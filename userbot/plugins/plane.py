# By STARKTM1
import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"plane"))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("✈-------------")
    await asyncio.sleep(1)
    await event.edit("-✈------------")
    await asyncio.sleep(1)
    await event.edit("--✈-----------")
    await asyncio.sleep(1)
    await event.edit("---✈----------")
    await asyncio.sleep(1)
    await event.edit("----✈---------")
    await asyncio.sleep(1)
    await event.edit("-----✈--------")
    await asyncio.sleep(1)
    await event.edit("------✈-------")
    await asyncio.sleep(1)
    await event.edit("-------✈------")
    await asyncio.sleep(1)
    await event.edit("--------✈-----")
    await asyncio.sleep(1)
    await event.edit("---------✈----")
    await asyncio.sleep(1)
    await event.edit("----------✈---")
    await asyncio.sleep(1)
    await event.edit("-----------✈--")
    await asyncio.sleep(1)
    await event.edit("------------✈-")
    await asyncio.sleep(1)
    await event.edit("-------------✈")
    await asyncio.sleep(5)
    await event.delete()
