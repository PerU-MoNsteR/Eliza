import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions

from userbot.utils import admin_cmd, eor, sudo_cmd

DEL_TIME_OUT = 60


@borg.on(admin_cmd(pattern="autobio"))
@borg.on(sudo_cmd(pattern="bio", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | I am Pro @Elizasupport01 | ⌚️ {HM}"
        logger.info(bio)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    about=bio
                )
            )
            await eor(event, "Autobio Enabled !!")
            await asyncio.sleep(2)
            await event.delete()
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
        # logger.info(r.stringify())
        # await borg.send_message(  # pylint:disable=E0602
        # Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        # "Successfully Changed Profile Bio"
        # )
        await asyncio.sleep(DEL_TIME_OUT)
