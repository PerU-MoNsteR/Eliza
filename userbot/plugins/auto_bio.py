"""
.autobio"""


import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions

from userbot.utils import admin_cmd

BIO_MSG = Config.BIO_MSG
if BIO_MSG is None:
    BIO_MSG = "I am a pro @eliza_support"

DEL_TIME_OUT = 60


@borg.on(admin_cmd(pattern="autobio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅{DMY} {BIO_MSG} ⌚️{HM}"
        logger.info(bio)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    about=bio
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
        # logger.info(r.stringify())
        # await borg.send_message(  # pylint:disable=E0602
        #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        #     "Successfully Changed Profile Bio"
        # )
        await asyncio.sleep(DEL_TIME_OUT)
