from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import admin_cmd


@borg.on(admin_cmd("sg ?(.*)"))
async def _(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

        await event.edit("```Reply to any user message.```")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.edit("```reply to text message```")

        return

    chat = "@SangMataInfo_bot"

    reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return

    await event.edit("```Processing```")

    async with borg.conversation(chat) as conv:

        try:

            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )

            await borg.forward_messages(chat, reply_message)

            response = await response

        except YouBlockedUserError:

            await event.reply("```Please unblock @sangmatainfo_bot and try again```")

            return

        if response.text.startswith("Forward"):

            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )

        else:

            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd("fakemail ?(.*)"))
async def _(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

        await event.edit("```Reply to any user message.```")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.edit("```reply to text message```")

        return

    chat = "@fakemailbot"

    reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return

    await event.edit("```Processing```")

    async with borg.conversation(chat) as conv:

        try:

            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=177914997)
            )

            await borg.forward_messages(chat, reply_message)

            response = await response

        except YouBlockedUserError:

            await event.reply("```Please unblock @sangmatainfo_bot and try again```")

            return

        if response.text.startswith("send"):

            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )

        else:

            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd("ub ?(.*)"))
async def _(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

        await event.edit("```Reply to any user message.```")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.edit("```reply to text message```")

        return

    chat = "@uploadbot"

    reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return

    await event.edit("```Processing```")

    async with borg.conversation(chat) as conv:

        try:

            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=97342984)
            )

            await borg.forward_messages(chat, reply_message)

            response = await response

        except YouBlockedUserError:

            await event.reply("```Please unblock @sangmatainfo_bot and try again```")

            return

        if response.text.startswith("Hi!,"):

            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )

        else:

            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd("gid ?(.*)"))
async def _(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

        await event.edit("```Reply to any user message.```")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.edit("```reply to text message```")

        return

    chat = "@getidsbot"

    reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return

    await event.edit("```Processing```")

    async with borg.conversation(chat) as conv:

        try:

            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=186675376)
            )

            await borg.forward_messages(chat, reply_message)

            response = await response

        except YouBlockedUserError:

            await event.reply("```oh  shit```")

            return

        if response.text.startswith("Hello,"):

            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )

        else:

            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd("urban ?(.*)"))
async def _(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

        await event.edit("```Reply to any user message.```")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.edit("```reply to text message```")

        return

    chat = "@UrbanDictionaryBot"

    reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return

    await event.edit("```Processing```")

    async with borg.conversation(chat) as conv:

        try:

            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=185693644)
            )

            await borg.forward_messages(chat, reply_message)

            response = await response

        except YouBlockedUserError:

            await event.reply("```oh shitt ```")

            return

        if response.text.startswith("Hello,"):

            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )

        else:

            await event.edit(f"{response.message.message}")
