
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    fboot = f"fastboot"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{fboot} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.adb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    adb = f"adb"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{adb} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.afh(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    afh = f"afh"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{afh} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.aex(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    aex = f"aex"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{aex} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.aosip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    aosip = f"aosip"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{aosip} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.reapk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    reapk = f"reapk"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{reapk} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.am(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    am = f"am"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{am} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.aqua(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    aqua = f"aqua"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{aqua} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.arrow(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    arrow = f"arrow"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{arrow} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.aicp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    aicp = f"aicp"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{aicp} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.asus(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    asus = f"asus"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{asus} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.bootleg(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    bootleg = f"bootleg"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{bootleg} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.caf(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    caf = f"caf"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{caf} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.candy(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    candy = f"candy"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{candy} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.carbon(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    carbon = f"carbon"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{carbon} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.top(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    top = f"top"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{top} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.popular(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    popular = f"popular"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{popular} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.apk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    apk = f"apk"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{apk} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.discover(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    discover = f"discover"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{discover} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.colt(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    colt = f"colt"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{colt} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.cosp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    cosp = f"cosp"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{cosp} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.crdroid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    crdroid = f"crdroid"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{crdroid} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.ddump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    ddump = f"ddump"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{ddump} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.ddog(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    ddog = f"ddog"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{ddog} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.dev(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    dev = f"dev"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{dev} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.astudio(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    astudio = f"astudio"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{astudio} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.cs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    cs = f"cs"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{cs} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")


              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.deviceinfos(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    deviceinfos = f"deviceinfos"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{deviceinfos} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.codename(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    codename = f"codename"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{codename} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.specs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    specs = f"specs"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{specs} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.dotos(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    dotos = f"dotos"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{dotos} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.du(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    du = f"du"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{du} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.dump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    dump = f"dump"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{dump} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.evox(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    evox = f"evox"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{evox} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.fdroid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    fdroid = f"fdroid"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{fdroid} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.gapps(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    gapps = f"gapps"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{gapps} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.gcam(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    gcam = f"gcam"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{gcam} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.repos(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    repos = f"repos"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{repos} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.commits(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    commits = f"commits"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{commits} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.getdump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    getdump = f"getdump"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{getdump} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.ps(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    ps = f"ps"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{ps} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.gsi(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    gsi = f"gsi"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{gsi} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.havoc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    havoc = f"havoc"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{havoc} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.huawei(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    huawei = f"huawei"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{huawei} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.kraken(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    kraken = f"kraken"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{kraken} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.labs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    labs = f"labs"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{labs} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.licrog(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    licrog = f"licrog"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{licrog} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.lineage(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    lineage = f"lineage"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{lineage} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.magisk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    magisk = f"magisk"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{magisk} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.microg(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    microg = f"microg"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{microg} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.moto(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    moto = f"moto"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{moto} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.nanodroid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    nanodroid = f"nanodroid"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{nanodroid} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.omni(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    omni = f"omni"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{omni} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.op(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    op = f"op"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{op} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.oppo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    oppo = f"oppo"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{oppo} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.of(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    of = f"of"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{of} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.pe(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    pe = f"pe"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{pe} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.pdust(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    pdust = f"pdust"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{pdust} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.pixy(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    pixy = f"pixy"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{pixy} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.potato(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    potato = f"potato"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{potato} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.realme(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    realme = f"realme"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{realme} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.revenge(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    revenge = f"revenge"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{revenge} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.rr(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    rr = f"rr"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{rr} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.samdump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    samdump = f"samdump"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{samdump} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.sonydump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    sonydump = f"sonydump"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{sonydump} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.superior(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    superior = f"superior"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{superior} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.syberia(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    syberia = f"syberia"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{syberia} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.twrp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    twrp = f"twrp"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{twrp} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.viper(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    viper = f"viper"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{viper} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.devdb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    devdb = f"devdb"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{devdb} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.xiaomi(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    xiaomi = f"xiaomi"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{xiaomi} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.xposed(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    xposed = f"xposed"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{xposed} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.xtended(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    xtended = f"xtended"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{xtended} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
