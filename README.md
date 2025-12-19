# Yonu – Telegram File Uploader (CLI)

Yonu is a lightweight command-line tool that uploads a file to Telegram using a bot account.  
It is designed to be simple, fast, and script-friendly.

You run it like a normal Linux command:
```bash
yonu path/to/file.mkv
```

The file will be sent to a specified Telegram chat (user, group, or channel).


# Features

📤 Upload any file to Telegram (Maximum file size is 2gb)
⚡ Simple CLI usage
🤖 Uses Telegram Bot API via Pyrogram
🐧 Designed for Linux
🧩 Easy to integrate into scripts and automation workflows

# Requirements
Python 3.8+
A Telegram account
Telegram API credentials (https://my.telegram.org/apps)
A Telegram bot token (you can get it from (@BotFather)[https://t.me/BotFather] in Telegram)

Python dependencies:
pyrogram
tgcrypto (recommended for better performance)

# Installation
1. Clone the repository
```bash
git clone https://github.com/kxshira/yonu-telegram-uploader.git
cd yonu
```

if you dont have git on your linux install git first 

2. Install dependencies
```bash
pip install -r requirements.txt
```
or manually:
```bash
pip install pyrogram tgcrypto
```

# Configuration
Edit this lines in script and change them to your own credentials
```python
API_ID = 123456
API_HASH = "your_api_hash_here"
BOT_TOKEN = "your_bot_token_here"
CHAT_ID = 123456789
```
You can get:
`API_ID` and `API_HASH` from https://my.telegram.org
`BOT_TOKEN` from @BotFather
`CHAT_ID` using a Telegram ID bot or Pyrogram 


# Usage 
Make the script executable
```
chmod +x yonu.py
```

Move it to your PATH (optional but recommended)
```
sudo mv yonu.py /usr/local/bin/yonu
```

try to upload a file
```
yonu example.txt
```
If the file exists, it will be uploaded to Telegram.

# Notes

This tool runs as a one-shot command (not a background service).

Best suited for manual uploads or scripting.

Large files may take time depending on your connection and Telegram limits.


# Disclaimer

This project is not affiliated with Telegram.
Use responsibly and respect Telegram’s terms of service.
