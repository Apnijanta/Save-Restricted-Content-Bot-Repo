
#Join @devggn

import sys
from pyrogram import Client
from telethon.sync import TelegramClient
import uvloop
from config import API_ID, API_HASH, BOT_TOKEN

bot = TelegramClient('prrrrepo', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)

modi = Client(
    "modibot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    modi.start()
except Exception as e:
    sys.exit(1)

sigma = Client(
    "sigma",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    sigma.start()
except Exception as e:
    sys.exit(1)

sex = TelegramClient('reee', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

