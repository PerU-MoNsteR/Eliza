# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import asyncio
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path
from shutil import copyfile

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pymediainfo import MediaInfo
from telethon.tl.types import DocumentAttributeVideo

from userbot.utils import admin_cmd, edit_or_reply

from . import CMD_HELP, make_gif, progress, reply_id, runcmd, thumb_from_audio

PATH = os.path.join("./temp", "temp_vid.mp4")
thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


async def weblst_of_files(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all filenames.
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
    return files


def get_video_thumb(file, output=None, width=320):
    output = file + ".jpg"
    metadata = extractMetadata(createParser(file))
    p = subprocess.Popen(
        [
            "ffmpeg",
            "-i",
            file,
            "-ss",
            str(
                int((0, metadata.get("duration").seconds)[metadata.has("duration")] / 2)
            ),
            # '-filter:v', 'scale={}:-1'.format(width),
            "-vframes",
            "1",
            output,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    p.communicate()
    if not p.returncode and os.path.lexists(file):
        return output


def sortthings(contents, path):
    websort = []
    contents.sort()
    for file in contents:
        webpath = os.path.join(path, file)
        if os.path.isfile(webpath):
            websort.append(file)
    for file in contents:
        webpath = os.path.join(path, file)
        if os.path.isdir(webpath):
            websort.append(file)
    return websort


async def upload(path, event, udir_event, catflag=None):
    global uploaded
    webflag or False
    reply_to_id = await reply_id(event)
    if os.path.isdir(path):
        await event.client.send_message(
            event.chat_id,
            f"**Folder : **`{str(path)}`",
        )
        Files = os.listdir(path)
        Files = sortthings(Files, path)
        for file in Files:
            os.path.join(path, file)
            await upload(webpath, event, udir_event)
    elif os.path.isfile(path):
        caption_rts = os.path.basename(path)
        c_time = time.time()
        thumb = None
        if os.path.exists(thumb_image_path):
            thumb = thumb_image_path
        if not caption_rts.lower().endswith(".mp4"):
            await event.client.send_file(
                event.chat_id,
                path,
                caption=f"**File Name : **`{caption_rts}`",
                force_document=catflag,
                thumb=thumb,
                reply_to=reply_to_id,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, udir_event, c_time, "Uploading...", caption_rts)
                ),
            )
        else:
            metadata = extractMetadata(createParser(str(path)))
            duration = 0
            width = 0
            height = 0
            if metadata.has("duration"):
                duration = metadata.get("duration").seconds
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
            await event.client.send_file(
                event.chat_id,
                path,
                caption=f"**File Name : **`{caption_rts}`",
                thumb=thumb,
                force_document=catflag,
                reply_to=reply_to_id,
                supports_streaming=True,
                attributes=[
                    DocumentAttributeVideo(
                        duration=duration,
                        w=width,
                        h=height,
                        round_message=False,
                        supports_streaming=True,
                    )
                ],
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, udir_event, c_time, "Uploading...", caption_rts)
                ),
            )
        uploaded += 1


@borg.on(admin_cmd(pattern="upload (.*)", outgoing=True))
async def uploadir(event):
    global uploaded
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    path = Path(input_str)
    start = datetime.now()
    if not os.path.exists(path):
        await edit_or_reply(
            event,
            f"`there is no such directory/file with the name {path} to upload`",
        )
        return
    udir_event = await edit_or_reply(event, "Uploading....")
    if os.path.isdir(path):
        await edit_or_reply(udir_event, f"`Gathering file details in directory {path}`")
        uploaded = 0
        await upload(path, event, udir_event)
        end = datetime.now()
        ms = (end - start).seconds
        await udir_event.edit(
            f"`Uploaded {uploaded} files successfully in {ms} seconds. `"
        )
    else:
        await edit_or_reply(udir_event, f"`Uploading.....`")
        uploaded = 0
        await upload(path, event, udir_event)
        end = datetime.now()
        ms = (end - start).seconds
        await udir_event.edit(
            f"`Uploaded file {str(path)} successfully in {ms} seconds. `"
        )
    await asyncio.sleep(5)
    await udir_event.delete()


@bot.on(admin_cmd(pattern="uploadf (.*)", outgoing=True))
async def uploadir(event):
    global uploaded
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    path = Path(input_str)
    start = datetime.now()
    if not os.path.exists(path):
        await edit_or_reply(
            event,
            f"`there is no such directory/file with the name {path} to upload`",
        )
        return
    udir_event = await edit_or_reply(event, "Uploading....")
    if os.path.isdir(path):
        await edit_or_reply(udir_event, f"`Gathering file details in directory {path}`")
        uploaded = 0
        await upload(path, event, udir_event, catflag=True)
        end = datetime.now()
        ms = (end - start).seconds
        await udir_event.edit(
            f"`Uploaded {uploaded} files successfully in {ms} seconds. `"
        )
    else:
        await edit_or_reply(udir_event, f"`Uploading.....`")
        uploaded = 0
        await upload(path, event, udir_event, catflag=True)
        end = datetime.now()
        ms = (end - start).seconds
        await udir_event.edit(
            f"`Uploaded file {str(path)} successfully in {ms} seconds. `"
        )
    await asyncio.sleep(5)
    await udir_event.delete()


@borg.on(admin_cmd(pattern="circle ?(.*)", outgoing=True))
async def video_webfile(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if input_str:
        path = Path(input_str)
        if not os.path.exists(path):
            await edit_or_reply(
                event,
                f"`there is no such directory/file with the name {path} to upload`",
            )
            return
        webevent = await edit_or_reply(event, "`Converting to video note..........`")
        filename = os.path.basename(path)
        webfile = os.path.join("./temp", filename)
        copyfile(path, webfile)
    else:
        if not reply:
            await edit_delete(event, "`Reply to supported media`", 5)
            return
        if not (reply and (reply.media)):
            await edit_delete(event, "`Reply to supported Media...`", 5)
            return
        webevent = await edit_or_reply(event, "`Converting to video note..........`")
        webfile = await reply.download_media(file="./temp/")
    if not webfile.endswith((".mp4", ".tgs", ".mp3", ".mov", ".gif", ".opus")):
        os.remove(webfile)
        await edit_delete(webevent, "```Supported Media not found...```", 5)
        return
    if webfile.endswith((".mp4", ".tgs", ".mov", ".gif")):
        if webfile.endswith((".tgs")):
            hmm = await make_gif(webevent, webfile)
            if hmm.endswith(("@tgstogifbot")):
                os.remove(webfile)
                return await webevent.edit(hmm)
            os.rename(hmm, "./temp/circle.mp4")
            webfile = "./temp/circle.mp4"
        media_info = MediaInfo.parse(webfile)
        aspect_ratio = 1
        for track in media_info.tracks:
            if track.track_type == "Video":
                aspect_ratio = track.display_aspect_ratio
                height = track.height
                width = track.width
        if aspect_ratio != 1:
            crop_by = width if (height > width) else height
            await runcmd(f'ffmpeg -i {webfile} -vf "crop={crop_by}:{crop_by}" {PATH}')
        else:
            copyfile(webfile, PATH)
        if str(webfile) != str(PATH):
            os.remove(webfile)
    else:
        thumb_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
        webthumb = None
        try:
            webthumb = await reply.download_media(thumb=-1)
        except:
            webthumb = os.path.join("./temp", "thumb.jpg")
            await thumb_from_audio(webfile, webthumb)
        if webthumb is None:
            webthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, webthumb)
        if (
            webthumb is not None
            and not os.path.exists(webthumb)
            and os.path.exists(thumb_loc)
        ):
            webthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, webthumb)
        if webthumb is not None and os.path.exists(webthumb):
            await runcmd(
                f"ffmpeg -loop 1 -i {webthumb} -i {webfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf \"scale='iw-mod (iw,2)':'ih-mod(ih,2)',format=yuv420p\" -shortest -movflags +faststart {PATH}"
            )
            os.remove(webfile)
        else:
            os.remove(webfile)
            return await edit_delete(
                webevent, "`No thumb found to make it video note`", 5
            )
    if os.path.exists(PATH):
        webid = event.reply_to_msg_id
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            PATH,
            allow_cache=False,
            reply_to=webid,
            video_note=True,
            attributes=[
                DocumentAttributeVideo(
                    duration=60,
                    w=1,
                    h=1,
                    round_message=True,
                    supports_streaming=True,
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, webevent, c_time, "Uploading...", PATH)
            ),
        )
        os.remove(PATH)
    await webevent.delete()


CMD_HELP.update(
    {
        "upload": "**Plugin :** `upload`\
    \n\n  •  **Syntax :** `.upload path of file/folder`\
    \n  •  **Function : **__Uploads the file from the server or list of files from that folder as steamable__\
    \n\n  •  **Syntax :** `.uploadf path of file/folder`\
    \n  •  **Function : **__Uploads the file from the server or list of files from that folder as a file__\
    \n\n  •  **Syntax : **`.circle reply to media or path of media`\
    \n  •  **Function : **__Uploads video/audio as streamable from the server__"
    }
)
