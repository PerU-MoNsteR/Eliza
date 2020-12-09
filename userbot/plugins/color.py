#  Fixed to use for all userbots-by @peru_monster
# Made for Eliza


import os

import requests

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="co$", outgoing=True))
async def detect(event):
    if Config.DEEP_AI is None:
        return await event.edit("Add VAR DEEP_AI get Api Key from https://deepai.org/")

    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("Reply to any image or non animated sticker !")
    await event.edit("Downloading the file to check...")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "catp")):
        return await event.edit("Reply to any image or non animated sticker !")
    devent = await event.edit("coloring image sar...")
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": Config.DEEP_AI},
    )
    os.remove(media)
    if "status" in r.json():
        return await devent.edit(r.json()["status"])
    r_json = r.json()["output_url"]
    pic_id = r.json()["id"]

    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"{r_json}"

    await devent.delete()
    await borg.send_message(event.chat_id, file=result)
