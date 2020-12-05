# Credits to @spechide and his team for @TROLLVOICEBOT

import re

from userbot import bot
from userbot.utils import admin_cmd

IF_EMOJI = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:

    """Remove emojis and other non-safe characters from string"""

    return re.sub(IF_EMOJI, "", inputString)


@borg.on(admin_cmd(pattern="mev(?: |$)(.*)"))
async def nope(per):
    bell = per.pattern_match.group(1)
    if not bell:
        if per.is_reply:
            (await per.get_reply_message()).message
        else:
            await per.edit(
                "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(hell))}")

    await troll[0].click(
        per.chat_id,
        reply_to=per.reply_to_msg_id,
        silent=True if per.is_reply else False,
        hide_via=True,
    )

    await per.delete()
