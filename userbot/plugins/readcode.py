#  (c)2020 Jarvis-Works
#
#thanks @sppidy
# By @buddhhu, @Itzsjdude ,@xditya
#
import os

from jarvis.utils import admin_cmd, eor, sudo_cmd


@borg.on(admin_cmd(pattern=r"reveal", outgoing=True))
@borg.on(sudo_cmd(pattern=r"reveal", allow_sudo=True))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    await eor(event, "**Reading file...**")
    if len(c) > 4095:
        await event.edit("`The Total words in this file is more than telegram limits.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
    os.remove(b)
