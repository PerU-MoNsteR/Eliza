from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"hhi ?(.*)"))
async def hhi(event):
    giveVar = event.text
    web = giveVar[5:6]
    if not web:
        web = "🌺"
    ct = giveVar[7:8]
    if not ct:
        ct = "✨"
    await event.edit(
        f"{web}{ct}{ct}{web}{ct}{web}{web}{web}\n{web}{ct}{ct}{web}{ct}{ct}{web}{ct}\n{web}{web}{web}{web}{ct}{ct}{web}{ct}\n{web}{ct}{ct}{web}{ct}{ct}{web}{ct}\n{web}{ct}{ct}{web}{ct}{web}{web}{web}\n☁☁☁☁☁☁☁☁"
    )
