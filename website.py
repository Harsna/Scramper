HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zenova CC Scrapper</title>
    <style>
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

header .logo img {
    width: 100px;
    margin-bottom: 10px;
}

h1 {
    font-size: 2.5em;
    margin: 0;
}

p {
    font-size: 1.1em;
}

section {
    padding: 20px;
    margin: 20px auto;
    max-width: 800px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
    font-size: 2em;
    border-bottom: 2px solid #333;
    padding-bottom: 10px;
}

ul {
    list-style-type: none;
    padding: 0;
}

ul li {
    padding: 10px 0;
    border-bottom: 1px solid #ddd;
}

ul li:last-child {
    border-bottom: none;
}

a {
    color: #0066cc;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
    width: 100%;
    bottom: 0;
}
</style>
</head>
<body>
    <header>
        <div class="logo">
            <a href="https://t.me/your_bot_username">
                <img src="https://te.legra.ph/file/a30f30e46ef1e58270ab2.jpg" alt="Zenova Logo">
            </a>
        </div>
        <h1>Zenova CC Scrapper</h1>
        <p>A Telegram Bot for Credit Card Validation and Posting 🤖</p>
    </header>

    <section id="introduction">
        <h2>Introduction</h2>
        <p>The Zenova CC Scrapper is a Telegram bot designed to scrape credit card information from various groups and channels on Telegram, validate the cards, and post them to a designated channel 📣. It leverages the Telethon library to interact with the Telegram API and perform tasks such as sending messages and processing incoming messages 📲.</p>
    </section>

    <section id="features">
        <h2>Features</h2>
        <ul>
            <li><strong>Card scraping:</strong> Scrape credit card information from various groups and channels on Telegram 📊</li>
            <li><strong>Card validation:</strong> Validate the scraped credit card information to ensure accuracy 💯</li>
            <li><strong>Posting:</strong> Post the validated credit card information to a designated channel on Telegram 📣</li>
            <li><strong>Error handling:</strong> Handle flood wait errors with multiple bots and retry mechanism 🔄</li>
            <li><strong>Performance metrics:</strong> Calculate time taken to process each transaction⏱️</li>
        </ul>
    </section>

    <section id="license">
        <h2>License</h2>
        <p>This script is licensed under the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache License 2.0</a> 📜. See the <a href="#">LICENSE</a> file for more information.</p>
    </section>

    <section id="disclaimer">
        <h2>Disclaimer</h2>
        <p>This script is for <strong>educational purposes only</strong> and should not be used for illegal activities 🚫. The author is not responsible for any misuse of this script.</p>
    </section>

    <footer>
        <p>&copy; 2024 Zenova CC Scrapper. All rights reserved.</p>
    </footer>
</body>
</html>

"""