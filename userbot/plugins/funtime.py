#idea from sandy
#base by peru_monster
import nekos

from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import CMD_HELP


@borg.on(admin_cmd(pattern="tques$"))
async def hmm(web):
    if web.fwd_from:
        return
    reactweb = nekos.textweb()
    await edit_or_reply(web, reactweb)


@borg.on(admin_cmd(pattern="why$"))
async def hmm(web):
    if web.fwd_from:
        return
    whyweb = nekos.why()
    await edit_or_reply(web, whyweb)


@bot.on(admin_cmd(pattern="fact$"))
@bot.on(sudo_cmd(pattern="fact$", allow_sudo=True))
async def hmm(web):
    if web.fwd_from:
        return
    factweb = nekos.fact()
    await edit_or_reply(web, factweb)


CMD_HELP.update(
    {
        "funtxts": """**Plugin : **`funtxts`
  •  **Syntax : **`.tcat`
  •  **Function : **__Sens you some random web facial text art__
  •  **Syntax : **`.why`
  •  **Function : **__Asks some random Funny questions__
  •  **Syntax : **`.fact`
  •  **Function : **__Sends you some random facts__"""
    }
)
