"""
Available Commands: .destroy
by @peru_monster"""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 21)

    input_str = event.pattern_match.group(1)

    if input_str == "destroy":

        await event.edit(input_str)

        animation_chars = [
            "`bot destroying syndrome successfully started!🤖🤖 `",
            "` user's bot will be destroyed in... 🔥`",
            "`10..⚙`",
            "`9..⚙`",
            "`8..⚙`",
            "`7..⚙`",
            "`6..⚙`",
            "`5..⚙`",
            "`4..⚙`",
            "`3..⚙`",
            "`2..⚙`",
            "`1😈`",
            "`🎆`",
            "`🌋`",
            "`B O O M`",
            "`TARGET USERS BOT IS DESTROYED SUCCESSFULLY😈👿`",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 100])
