import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "avengers User"
PM_IMG = "https://telegra.ph/file/ced30b3600c5a4e6b2d8a.jpg"
pm_caption = "🔱 **ELIZA Is Online** 🔱\n\n"

pm_caption += f"🔸🔹 **ɱყ ცơʂʂ**           :   {DEFAULTUSER}\n"

pm_caption += "🔹🔸 тєℓєтнσи νєяѕισи   :   1.15.0 \n"

pm_caption += "🔸🔹 σffι¢ιαℓ ¢нαииєℓ   :   [ᴊᴏɪɴ](https://t.me/eliza_support_channel)\n"

pm_caption += "🔹🔸 σffι¢ιαℓ gяσυρ     :   [ᴊᴏɪɴ](https://t.me/eliza_support)\n"

pm_caption += "🔸🔹 ℓι¢єиѕє            :   [ӀíϲҽղՏҽ](https://github.com/The-Avengers-leader/Eliza/blob/master/LICENSE)\n"

pm_caption += "🔹🔸 ¢σρуяιgнт          :   [ELIZA](https:/The-Avengers-leader/github.com/)\n"

pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/eliza_suport)\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
