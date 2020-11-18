#plugin by @peru_monster(Charlie Puth)
#set var  PERU_PIC and PERU_USERNAME in heroku to work for your wish

import asyncio
import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from userbot.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

PERU_PIC = os.environ.get("SUR_PIC", None)
if PERU_PIC is None:
    PERU_PIC = "https://telegra.ph/file/4e45d2e7500fe03c89651.jpg"
else:
    PERU_PIC = PERU_PIC
PERU_USERNAME = os.environ.get("PERU_USERNAME", None)
PERU_USERNAME = str(PERU_USERNAME) if PERU_USERNAME else "@PERU_MONSTER"


@bot.on(admin_cmd(pattern="peru$"))
async def autopic(event):
    await event.edit(f"Autopic plugin made by @peru_monster")
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(PERU_PIC, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        pass
    while True:
        shutil.copy(downloaded_file_name, photo)
        img = Image.open(photo)
        current_time = datetime.now().strftime(
            f"{PERU_USERNAME} \n \nTime: %H:%M:%S \nDate: %d/%m/%y"
        )
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((50, 400), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return
