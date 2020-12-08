# base by peru_monster
import nekos

from userbot import CMD_HELP
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@borg.on(admin_cmd(pattern="why$"))
async def hmm(web):
    if web.fwd_from:
        return
    whyweb = nekos.why()
    await edit_or_reply(web, whyweb)


@borg.on(admin_cmd(pattern="fact$"))
async def hmm(web):
    if web.fwd_from:
        return
    factweb = nekos.fact()
    await edit_or_reply(web, factweb)
