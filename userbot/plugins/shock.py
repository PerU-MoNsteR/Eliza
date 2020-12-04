"""Emoji
Available Commands:
.shock"""

import asyncio

from userbot.utils import admin_cmd


@peru.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 11)
    input_str = event.pattern_match.group(1)
    if input_str == "shock":
        await event.edit(input_str)
        animation_chars = [
            "ME: 😂",
            "ME: 😄",
            "ME: 😀",
            "ME: 🙂",
            "ME: 😐",
            "ME: 🙁",
            "ME: 😟",
            "ME: 😧",
            "ME: 😨",
            "ME: 😰",
            "ME: 😱",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])
