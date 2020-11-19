import os
import time
import asyncio
import shutil
import json
from bs4 import BeautifulSoup
import re
from html import unescape
from re import findall
from urllib.parse import quote_plus
from urllib.error import HTTPError
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
from urbandict import define
from requests import get
from search_engine_parser import GoogleSearch
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googletrans import LANGUAGES, Translator
from gtts import gTTS
from gtts.lang import tts_langs
from emoji import get_emoji_regexp
from youtube_search import YoutubeSearch
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from userbot import (CMD_HELP, BOTLOG, BOTLOG_CHATID,
                     TEMP_DOWNLOAD_DIRECTORY)
from userbot.events import register
from telethon.tl.types import DocumentAttributeAudio
from userbot.helpers import progress, chrome, googleimagesdownload

CARBONLANG = "auto"
TTS_LANG = "id"
TRT_LANG = "id"

@register(outgoing=True, pattern=r"^\.tts(?: |$)([\s\S]*)")
async def text_to_speech(query):
    """ For .tts command, a wrapper for Google Text-to-Speech. """
    textx = await query.get_reply_message()
    message = query.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await query.edit(
            "`Give a text or reply to a message for Text-to-Speech!`")

    try:
        gTTS(message, lang=TTS_LANG)
    except AssertionError:
        return await query.edit(
            'The text is empty.\n'
            'Nothing left to speak after pre-precessing, tokenizing and cleaning.'
        )
    except ValueError:
        return await query.edit('Language is not supported.')
    except RuntimeError:
        return await query.edit('Error loading the languages dictionary.')
    tts = gTTS(message, lang=TTS_LANG)
    tts.save("k.mp3")
    with open("k.mp3", "rb") as audio:
        linelist = list(audio)
        linecount = len(linelist)
    if linecount == 1:
        tts = gTTS(message, lang=TTS_LANG)
        tts.save("k.mp3")
    with open("k.mp3", "r"):
        await query.client.send_file(query.chat_id, "k.mp3", voice_note=True)
        os.remove("k.mp3")
        if BOTLOG:
            await query.client.send_message(
                BOTLOG_CHATID, "`Sudah Di Ubah Bro wkwkw`")
        await query.delete()

@register(outgoing=True, pattern=r"^\.tr(?: |$)([\s\S]*)")
async def translateme(trans):
    """ For .trt command, translate the given text using Google Translate. """
    translator = Translator()
    textx = await trans.get_reply_message()
    message = trans.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await trans.edit("`Kasih text atau bales pesan untuk translate!`")

    try:
        reply_text = translator.translate(deEmojify(message), dest=TRT_LANG)
    except ValueError:
        return await trans.edit("Invalid destination language.")

    source_lan = LANGUAGES[f'{reply_text.src.lower()}']
    transl_lan = LANGUAGES[f'{reply_text.dest.lower()}']
    reply_text = f"Source. : **{source_lan.title()}**\nKe.         : **{transl_lan.title()}**\n\n{reply_text.text}"

    await trans.edit(reply_text)
    if BOTLOG:
        await trans.client.send_message(
            BOTLOG_CHATID,
            f"Translated some {source_lan.title()} stuff to {transl_lan.title()} just now.",
        )


@register(pattern=".lang (tr|tts) (.*)", outgoing=True)
async def lang(value):
    """ For .lang command, change the default langauge of userbot scrapers. """
    util = value.pattern_match.group(1).lower()
    if util == "tr":
        scraper = "Translator"
        global TRT_LANG
        arg = value.pattern_match.group(2).lower()
        if arg in LANGUAGES:
            TRT_LANG = arg
            LANG = LANGUAGES[arg]
        else:
            return await value.edit(
                f"`Invalid Language code !!`\n`Available language codes for TRT`:\n\n`{LANGUAGES}`"
            )
    elif util == "tts":
        scraper = "Text to Speech"
        global TTS_LANG
        arg = value.pattern_match.group(2).lower()
        if arg in tts_langs():
            TTS_LANG = arg
            LANG = tts_langs()[arg]
        else:
            return await value.edit(
                f"`Invalid Language code !!`\n`Available language codes for TTS`:\n\n`{tts_langs()}`"
            )
    await value.edit(f"`Bahasa untuk **{scraper}** berubah menjadi **{LANG.title()}**.`")
    await asyncio.sleep(2)
    await value.delete()
    if BOTLOG:
        await value.client.send_message(
            BOTLOG_CHATID,
            f"`Bahasa untuk {scraper} berubah menjadi {LANG.title()}.`")
        await asyncio.sleep(3)
        await value.delete()

YOUTUBE_API_KEY = "AIzaSyCT8eXHkbJ3N2al7spP69nseRmYk5U1VHU"
@register(outgoing=True, pattern=r"^\.yt (\d*) *(.*)")
async def yt_search(video_q):
    """For .yt command, do a YouTube search from Telegram."""
    if video_q.pattern_match.group(1) != "":
        counter = int(video_q.pattern_match.group(1))
        if counter > 10:
            counter = int(10)
        if counter <= 0:
            counter = int(1)
    else:
        counter = int(10)

    query = video_q.pattern_match.group(2)
    if not query:
        await video_q.edit("`Enter query to search`")
    await video_q.edit("`Processing...`")

    try:
        results = json.loads(
            YoutubeSearch(
                query,
                max_results=counter).to_json())
    except KeyError:
        return await video_q.edit("`Youtube Search gone retard.\nCan't search this query!`")

    output = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n"

    for i in results["videos"]:
        try:
            title = i["title"]
            link = "https://youtube.com" + i["url_suffix"]
            channel = i["channel"]
            duration = i["duration"]
            views = i["views"]
            output += f"[{title}]({link})\nChannel: `{channel}`\nDuration: {duration} | {views}\n\n"
        except IndexError:
            break

    await video_q.edit(output, link_preview=False)


def deEmojify(inputString):
    """ Remove emojis and other non-safe characters from string """
    return get_emoji_regexp().sub(u'', inputString)

import os
import time
import math
import asyncio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from telethon.tl.types import DocumentAttributeAudio
from uniborg.util import admin_cmd

async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            ''.join(["▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]

@borg.on(admin_cmd(pattern="yt(a|v) (.*)"))
async def download_video(v_url):
    """ For .ytdl command, download media from YouTube and many other sites. """
    url = v_url.pattern_match.group(2)
    type = v_url.pattern_match.group(1).lower()

    await v_url.edit("`Preparing to download...`")

    if type == "a":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '480',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True

    elif type == "v":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True

    try:
        await v_url.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await v_url.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await v_url.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await v_url.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await v_url.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await v_url.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await v_url.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await v_url.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await v_url.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await v_url.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await v_url.edit(f"`Preparing to upload song:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(ytdl_data['duration']),
                                       title=str(ytdl_data['title']),
                                       performer=str(ytdl_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{ytdl_data['title']}.mp3")))
        os.remove(f"{ytdl_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await v_url.edit(f"`Preparing to upload video:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp4",
            supports_streaming=True,
            caption=ytdl_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{ytdl_data['title']}.mp4")))
        os.remove(f"{ytdl_data['id']}.mp4")
        await v_url.delete()

import os
import lyricsgenius
from userbot.utils import admin_cmd
from userbot import CMD_HELP
from tswift import Song
import io
GENIUS = "UtpWEjKWPfAkuFrC3SmkCpFSHVF2p2bvmR-6029Y4M6rCnDBJCGFKrOzUh-D1XQA"


@borg.on(admin_cmd(outgoing=True, pattern="lyrics ?(.*)"))
async def lyrics(lyric):
    if lyric.pattern_match.group(1):
        query = lyric.pattern_match.group(1)
    else:
        await lyric.edit("Error: please use '-' as divider for <artist> and <song> \neg: `.glyrics Nicki Minaj - Super Bass`")
        return
    if r"-" in query:
        pass
    else:
        await lyric.edit("Error: please use '-' as divider for <artist> and <song> \neg: `.glyrics Nicki Minaj - Super Bass`")
        return
    if GENIUS is None:
        await lyric.edit("`Provide genius access token to config.py or Heroku Var first kthxbye!`")
    else:
        genius = lyricsgenius.Genius(GENIUS)
        try:
            args = query.split('-', 1)
            artist = args[0].strip(' ')
            song = args[1].strip(' ')
        except Exception as e:
            await lyric.edit(f"Error:\n`{e}`")
            return
    if len(args) < 1:
        await lyric.edit("`Please provide artist and song names`")
        return
    await lyric.edit(f"`Searching lyrics for {artist} - {song}...`")
    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None
    if songs is None:
        await lyric.edit(f"Song **{artist} - {song}** not found!")
        return
    if len(songs.lyrics) > 4096:
        await lyric.edit("`Lyrics is too big, view the file to see it.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
    else:
        await lyric.edit(f"**Search query**: \n`{artist} - {song}`\n\n```{songs.lyrics}```")
    return

CMD_HELP.update(
    {"lyrics": "Lyrics Plugin Syntax: `.lyrics` <aritst name - song nane> or `.lyrics` <song_name>\
    \n**USAGE:** searches a song lyrics and sends you if song name doesnt work try along with artisyt name\
    \n\n**Usage:** .`glyrics <artist name> - <song name>`\
    \n__note__: **-** is neccessary when searching the lyrics to divided artist and song\
    \n\n**Genius lyrics plugin**\
    \nget this value from `https://genius.com/developers` \
    \nAdd:-  `GENIUS_API_TOKEN` and token value in heroku app settings \
    "})

CMD_HELP.update({
    "img":
    ">`.img <search_query>`"
    "\nUsage: Does an image search on Google and shows 5 images.",
    "currency":
    ">`.currency <amount> <from> <to>`"
    "\nUsage: Converts various currencies for you.",
    "carbon":
    ">`.carbon <text> [or reply]`"
    "\nUsage: Beautify your code using carbon.now.sh\n"
    "Use .crblang <text> to set language for your code.",
    "google":
    ">`.google <query>`"
    "\nUsage: Does a search on Google.",
    "wiki":
    ">`.wiki <query>`"
    "\nUsage: Does a search on Wikipedia.",
    "ud":
    ">`.ud <query>`"
    "\nUsage: Does a search on Urban Dictionary.",
    "tts":
    ">`.tts <text> [or reply]`"
    "\nUsage: Translates text to speech for the language which is set."
    "\nUse >`.lang tts <language code>` to set language for tts. (Default is English.)",
    "trt":
    ">`.trt <text> [or reply]`"
    "\nUsage: Translates text to the language which is set."
    "\nUse >`.lang trt <language code>` to set language for trt. (Default is English)",
    "yt":
    ">`.yt <text>`"
    "\nUsage: Does a YouTube search.",
    "imdb":
    ">`.imdb <movie-name>`"
    "\nUsage: Shows movie info and other stuff.",
    "rip":
    ">`.ripaudio <url> or ripvideo <url>`"
    "\nUsage: Download videos and songs from YouTube "
    "(and [many other sites](https://ytdl-org.github.io/youtube-dl/supportedsites.html))."
})
