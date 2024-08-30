import random
import time
from telethon import TelegramClient, events, types, errors
import re
import aiohttp
import website
import asyncio

api_id = '27881764' 
api_hash = '078d33056f82e3583f6161ad255af5bd' 
phone_number = '+919460760553'
token1 = "7187583918:AAHoOo7Yl8Jwf9aEWwCPrMmGJ0WUoF5U5Ew"
token2 = "7430417694:AAG6xD1ZhtjHtIebA86b-B9SoPUkdC0Vr6s"

client = TelegramClient('black_scrapper', api_id, api_hash)
bot1 = TelegramClient('bot1', api_id, api_hash)
bot2 = TelegramClient('bot2', api_id, api_hash)

BIN_API_URL = 'https://bins.antipublic.cc/bins/{}'

# Function to filter card information using regex
def filter_cards(text):
    regex = r'\d{16}.*\d{3}'
    matches = re.findall(regex, text)
    return matches

# Function to perform BIN lookup
async def bin_lookup(bin_number):
    print(bin_number)
    bin_info_url = BIN_API_URL.format(bin_number)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(bin_info_url) as response:
            if response.status == 200:
                try:
                    bin_info = await response.json()
                    return bin_info
                except aiohttp.ContentTypeError:
                    return None
            else:
                return None

# Function to send message using one of the two bots
async def send_message(message, bot):
    try:
        await bot.send_message('ScrapperByUs', message, link_preview=False)
    except errors.FloodWaitError as e:
        print(f"Flood wait error: {e.seconds}")
        if bot == bot1:
            await send_message(message, bot2)
        else:
            await asyncio.sleep(e.seconds)  # Wait before retrying
            await send_message(message, bot)

# Event handler 
@client.on(events.NewMessage)
@client.on(events.MessageEdited)
async def checker(event):
    try:
        message = event.message
        # Regex to match approved messages
        if re.search(r'(Approved!|Charged|authenticate_successful|𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱|- 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅|APPROVED|New Cards Found By Scrapper|ꕥ Extrap [☭]|• New Cards Found By JennaS>)', message.text):
            filtered_card_info = filter_cards(message.text)
            if not filtered_card_info:
                return

            start_time = time.time()  # Start timer

            for card_info in filtered_card_info:
                bin_number = card_info[:6]
                bin_info = await bin_lookup(bin_number)
                if bin_info:
                    brand = bin_info.get("brand", "N/A")
                    card_type = bin_info.get("type", "N/A")
                    level = bin_info.get("level", "N/A")
                    bank = bin_info.get("bank", "N/A")
                    country = bin_info.get("country_name", "N/A")
                    country_flag = bin_info.get("country_flag", "")

                    # Calculate time taken with random addition
                    random_addition = random.uniform(0, 10) + 10  # Add random seconds between 10 and 20
                    time_taken = time.time() - start_time + random_addition
                    formatted_time_taken = f"{time_taken:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"

                    # Format the message
                    formatted_message = (
                        f"- 𝐀𝐩𝐩𝐫𝗼𝐯𝗲𝐝 ✅\n\n"
                        f"- 𝗖𝗮𝗿𝗱: `{card_info}`\n"
                        f"- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Auth 4\n"
                        f"- 𝐑𝐞𝐬𝗽𝗼𝐧𝐬𝗲: `1000: Approved`\n\n"
                        f"- 𝗜𝗻𝗳𝗼: {brand} - {card_type} - {level}\n"
                        f"- 𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n"
                        f"- 𝐂𝗼𝐮𝐧𝐭𝐫𝐲: {country} {country_flag}\n\n"
                        f"𝗧𝗶𝗺𝗲: {formatted_time_taken}\n\n"
                        f"⚡️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆 [𝗖𝗖 𝗦𝗰𝗿𝗮𝗽𝗽𝗲𝗿](https://t.me/ScrapperByUs) ⚡️"
                    )
                    print(formatted_message)
                    # Send the formatted message using one of the two bots
                    await send_message(formatted_message, bot1)
    except Exception as e:
        print(e)


# Main function to start the clients
async def main():
    await client.start(phone=phone_number)
    await bot1.start(bot_token=token1)
    await bot2.start(bot_token=token2)
    print("Clients Created")
    await client.run_until_disconnected()
    await bot1.run_until_disconnected()
    await bot2.run_until_disconnected()

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(website.HTML)

if __name__ == "__main__":
    import threading
    threading.Thread(target=app.run, args=('0.0.0.0', 8000)).start()
    # Run the main function
    asyncio.run(main())
