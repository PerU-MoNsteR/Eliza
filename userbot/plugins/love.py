#Credit To @M_R_S_P_I_D_Y 


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="ilu ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("I")
        await asyncio.sleep(0.7)
        await event.edit("I L")
        await asyncio.sleep(0.7)
        await event.edit("I LO")
        await asyncio.sleep(0.7)
        await event.edit("I LOV")
        await asyncio.sleep(0.7)
        await event.edit("I LOVE")
        await asyncio.sleep(0.7)
        await event.edit("I LOVE Y")
        await asyncio.sleep(0.7)
        await event.edit("I LOVE YO")
        await asyncio.sleep(0.7)
        await event.edit("I LOVE YOU")
        await asyncio.sleep(0.7)
      
        await event.edit("** I LOVE YOU**💓💓😘😘")
