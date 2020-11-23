import random

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, permemes


@bot.on(admin_cmd(pattern=f"gm$", outgoing=True))
@bot.on(sudo_cmd(pattern="gm$", allow_sudo=True))
async def morning(morning):
    txt = random.choice(permemes.GDMORNING)
    await edit_or_reply(morning, txt)


@bot.on(admin_cmd(pattern=f"gnoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="gnoon$", allow_sudo=True))
async def noon(noon):
    txt = random.choice(permemes.GDNOON)
    await edit_or_reply(noon, txt)


@bot.on(admin_cmd(pattern=f"gn$", outgoing=True))
@bot.on(sudo_cmd(pattern="gn$", allow_sudo=True))
async def night(night):
    txt = random.choice(permemes.GDNIGHT)
    await edit_or_reply(night, txt)


@bot.on(admin_cmd(pattern="gmg$"))
@bot.on(sudo_cmd(pattern="gmg$", allow_sudo=True))
async def gm(event):
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
    )


@bot.on(admin_cmd(pattern="gnt$"))
@bot.on(sudo_cmd(pattern="gnt$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･",
    )


@bot.on(admin_cmd(pattern=r"cheer$"))
@bot.on(sudo_cmd(pattern="cheer$", allow_sudo=True))
async def cheer(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )


@bot.on(admin_cmd(pattern=r"getwell$"))
@bot.on(sudo_cmd(pattern="getwell$", allow_sudo=True))
async def getwell(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )


@bot.on(admin_cmd(pattern=r"luck$"))
@bot.on(sudo_cmd(pattern="luck$", allow_sudo=True))
async def luck(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )


@bot.on(admin_cmd(pattern=r"sprinkle$"))
@bot.on(sudo_cmd(pattern="sprinkle$", allow_sudo=True))
async def sprinkle(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀",
    )


CMD_HELP.update(
    {
        "greetings": """**Plugin : **`greetings`
**Syntax : **
  •  `.gm`
  •  `.gnoon`
  •  `.gn`  
**Function : **__sends you random good morning , afternoon and night quotes respectively.__
**Syntax : **
  •  `.gnt`
  •  `.gmg`
  •  `.hi/.hi emoji`
  •  `.cheer`
  •  `.getwell`
  •  `.luck`
  •  `.sprinkle`
**Function : **__shows you some text arts for these greeting commands.__"""
    }
)
