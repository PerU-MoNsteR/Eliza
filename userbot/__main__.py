"""import glob
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from . import LOGS, bot
from .Config import Config
from .utils import load_module
"""
  
import os
from pathlib import Path
from sys import argv
from .Config import Config

import telethon.utils
from telethon import TelegramClient
from . import LOGS, bot

from .utils import load_module, start_assistant
from var import Var

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialised Sucessfully")
        print("Starting JARVIS AI")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()


import glob

if LOAD_USERBOT == True:
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
else:
    print("Userbot is Not Loading As U Have Disabled")

if LOAD_ASSISTANT == True:
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
else:
    print("for queries contact me here https://t.me/Elizasupport01")

print("Efforts never fail, thank @peru_monster for this awesome Eliza userbot.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()




































"""before assisstant
    async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_USER_NAME_BF_HER is not None:
        LOGS.info("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN_BF_HER)
        LOGS.info("Initialisation finished with no errors")
        LOGS.info("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Config.TG_BOT_USER_NAME_BF_HER))
        LOGS.info("Startup Completed")
    else:
        bot.start()

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        if shortname.replace(".py", "") not in Config.NO_LOAD:
            load_module(shortname.replace(".py", ""))
            


LOGS.info("Efforts never fail, thank @peru_monster for this awesome Eliza userbot!!")
LOGS.info(
    "hurrah all completed now, type .alive to see message if bot is live\n"
    "for queries contact me here https://t.me/Elizasupport01"
)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
"""

