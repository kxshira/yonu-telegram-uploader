#!/usr/bin/env python3
from pyrogram import Client
import asyncio
import sys
import os

# ===============================
API_ID = 123456       # Replace with your API ID (from https://my.telegram.org)
API_HASH = "your_api_hash_here" # Replace with your API HASH (from https://my.telegram.org)
BOT_TOKEN = "your_bot_token_here" # Replace with your bot token from @botfather
CHAT_ID = 123456789   # Replace with your chat ID (can be group, channel, or user)
# ===============================

async def send_file(file_path):
    if not os.path.exists(file_path):
        print("ERROR - File not found:", file_path)
        return

    async with Client("uploader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN) as app:
        print(f"📤 Uploading {os.path.basename(file_path)} ...")
        await app.send_document(CHAT_ID, file_path)
        print("OK - Upload complete!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 upload_bot.py <file_path>")
        sys.exit(1)

    asyncio.run(send_file(sys.argv[1]))
