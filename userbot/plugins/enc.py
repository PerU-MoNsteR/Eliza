from telethon.tl.types import MessageMediaPhoto
import os, urllib, requests, re, asyncio
from userbot.utils import admin_cmd
from . import CMD_HELP, ALIVE_NAME

PERUMONSTER = Config.DEEP_AI if Config.DEEP_AI else "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"


WEBO_IS_ALIVE = str(ALIVE_NAME) if ALIVE_NAME else "Eliza"
@borg.on(admin_cmd(pattern="enc ?(.*)", outgoing=True))
async def _(event):                   
    reply = await event.get_reply_message()
    if not reply:

        return await event.edit(
           "Reply to any image or non animated sticker !"
        )

    input_str = event.pattern_match.group(1)
    hm = input_str 
    devent = await event.edit("yo let me downlaoad it....")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await event.edit(
             "Reply to any image or non animated sticker !"
        )
    
    if input_str:
        devent = await event.edit("styling...")
        r = requests.post(
          "https://api.deepai.org/api/neural-style",
        files={
            'style': f"{hm}",
            'content': open(media, "rb"),
            },
        headers={"api-key": PERUMONSTER},
    )

        os.remove(media)
        if "status" in r.json():
            return await devent.edit( r.json()["status"])
        r_json = r.json()['output_url']
        pic_id = r.json()['id']
    
        link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
        result = f"{r_json}"
    
        await devent.delete()
        await borg.send_message(
        event.chat_id,
        file=result)
    
    else:
      devent = await event.edit("styling...")
      r = requests.post(
          "https://api.deepai.org/api/neural-style",
      files={
            'style': 'https://telegra.ph/file/aaaa686bd3acff51208d7.jpg',
            'content': open(media, "rb"),
            },
      headers={"api-key": PERUMONSTER},
    )

      os.remove(media)
      if "status" in r.json():
          return await devent.edit( r.json()["status"])
      r_json = r.json()['output_url']
      pic_id = r.json()['id']
    
      link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
      result = f"{r_json}"
    
      await devent.delete()
      await borg.send_message(
      event.chat_id,
      file=result)


CMD_HELP.update(
    {
        "imgenc": 
    ".enc <reply to any anime media> "
    "\nIt enhancerize any anime pic (Note :-if its not working then go to deepai.org then get api and set var DEEP_AI nd key.)"
    })
