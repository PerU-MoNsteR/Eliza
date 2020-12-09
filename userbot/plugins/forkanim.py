import asyncio

from telethon import events

from userbot.utils import admin_cmd


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "fork":

        await event.edit(input_str)

        animation_chars = [
            "`Your bot is running\n\nTelethon version:` 1.9.0\n`Python:` 3.7.3\n`User:` @peru_monster\n`Database Status: Databases functioning normally!`",
            "`Connecting To github.com...`",
            "`Deleting existing Repo....`",
            "`Forking Eliza... 0%\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 0 MiB / 108.7 MiB`",
            "`Forking Eliza... 4%\n\n⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 22 MiB / 108.7 MiB`",
            "`Forking Eliza... 8%\n\n⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 48 MiB / 108.7 MiB`",
            "`Forking Eliza... 20%\n\n⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 55 MiB / 108.7 MiB`",
            "`Forking Eliza... 36%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 60 MiB / 108.7 MiB `",
            "`Forking Eliza... 52%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 90.7 MiB / 108.7 MiB `",
            "`Forking Eliza... 84%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️\n\nFile Size: 100.7 MiB / 108.7 MiB `",
            "`Forking Eliza... 100%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\n\nFile Size: 108.7 MiB / 108.7 MiB\n\nTask Completed... `",
            "`Fork Deploying...`\n\n@Eliza_support_group ( `Custom Built By` @peru_monster ) \n`Verified Account:` ☑️\n`Repo: https://github.com/PerU-MoNsteR/Eliza`\n\n`Python` `Loading...`\n[GCC 7.4.0]\n`Telethon` `Loading...`\n\n`Custom Built Fork:` `Loading...`",
            "`Fork Deployed...`\n\n@Eliza_support_group ( `Custom Built By` @peru_monster ) \n`Verified Account:` ✅\n`Repo:` https://github.com/PerU-MoNsteR/Eliza\n\n`Python` 3.8.6 (default, jan 2020, 01:19:52)\n[GCC 8.4.0]\n`Telethon` 1.16.0\n\n`Custom Built Fork:` https://github.com/PerU-MoNsteR/Eliza",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])


@borg.on(admin_cmd("nope"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "nope":
    await event.edit("nope")
    animation_chars = [
        "No",
        "Problem",
        "Boss",
        "Yeah ! No problem",
        "No Problem Boss.lol",
        "No Problem Boss😇.Lol",
        "No Problem Man😇.Lol",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="f"))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await event.edit(pay)
    
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="frwd"))
async def _(event):
    if event.fwd_from:
        return
    if Config.PRIVATE_CHANNEL_BOT_API_ID is None:
        await event.edit(
            "Please set the required environment variable `PRIVATE_CHANNEL_BOT_API_ID` for this plugin to work"
        )
        return
    try:
        e = await borg.get_entity(Config.PRIVATE_CHANNEL_BOT_API_ID)
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await borg.forward_messages(e, re_message, silent=True)
        await borg.forward_messages(event.chat_id, fwd_message)
        await fwd_message.delete()
        await event.delete()

