#plugin by @peru_monster(Charlie Puth)
#set var  PERU_PIC and PERU_USERNAME in heroku to work for your wish

import asyncio
import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from userbot.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

PERU_PIC = os.environ.get("SUR_PIC", None)
if PERU_PIC is None:
    PERU_PIC = "https://telegra.ph/file/4e45d2e7500fe03c89651.jpg"
else:
    PERU_PIC = PERU_PIC
PERU_USERNAME = os.environ.get("PERU_USERNAME", None)
PERU_USERNAME = str(PERU_USERNAME) if PERU_USERNAME else "@PERU_MONSTER"


@bot.on(admin_cmd(pattern="peru$"))
async def autopic(event):
    await event.edit(f"Autopic plugin made by @peru_monster")
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(PERU_PIC, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        pass
    while True:
        shutil.copy(downloaded_file_name, photo)
        img = Image.open(photo)
        current_time = datetime.now().strftime(
            f"{PERU_USERNAME} \n \nTime: %H:%M:%S \nDate: %d/%m/%y"
        )
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((50, 400), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return

        import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [
  "star-wars-wallpaper-1080p",
  "4k-sci-fi-wallpaper",
  "star-wars-iphone-6-wallpaper",
  "kylo-ren-wallpaper",
  "darth-vader-wallpaper"
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")
@borg.on(admin_cmd(pattern="gamerpfp ?(.*)"))
async def main(event):
    await event.edit("**Starting Gamer Profile Pic.**") #Owner @NihiNivi
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(30)
        
import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRINGZ = [
  "india-flag-wallpaper-2018",
  "indian-national-flag-wallpaper-3d",
  "indian-independence-day-hd-pic-wallpaper-2018"
]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("http://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="indiandp ?(.*)"))

async def main(event):

    await event.edit("**Starting 🇮🇳 Profile Pics [i.e ]...\n\nDone !!! Check Your DP !! Made by @peru_monster ") 

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(60)
       
 
"""
Time In Profile Pic.....
Command: `.perupfp`
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from userbot.utils import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/2eab4f64ead6fbf41bf87.jpg",
                         "https://telegra.ph/file/6bef1ffbaddc5230c2ae1.jpg",
                         "https://telegra.ph/file/a03f035e83098a7c5bded.jpg",
                         "https://telegra.ph/file/f0a230a30b9952f56d2cd.jpg",
                         "https://telegra.ph/file/d00e6bb4b4a483099c992.jpg",
                         "https://telegra.ph/file/1270ed675db61e6c84eea.jpg",
                         "https://telegra.ph/file/32743c9389915b02fdea7.jpg",
                         "https://telegra.ph/file/8c02a1430502bea931ff7.jpg",
                         "https://telegra.ph/file/1ec37d367bb59ac56131d.jpg",
                         "https://telegra.ph/file/e9aeef4fd2e3d0b9e9f24.jpg",
                         "https://telegra.ph/file/28c242ea9f8cf32db4c21.jpg",
                         "https://telegra.ph/file/c089426ca031d1f6297b0.jpg",
                         "https://telegra.ph/file/a196b6c07f0a659daf058.jpg",
                         "https://telegra.ph/file/69f19acd13b1eaf3fc120.jpg"
                        ]
@borg.on(admin_cmd(pattern="perupfp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("@peru_monster \n \nTime: %H:%M:%S \nDate: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((350, 400), current_time, font=fnt, fill=(230,230,250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(30)
        except:
            return
        
import os   
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/e354ce72d5cc6a1d27c4d.jpg", 
                         "https://telegra.ph/file/8f9ff3d743e6707a61489.jpg", 
                         "https://telegra.ph/file/bfc97f4abc4bec6fe860d.jpg", 
                         "https://telegra.ph/file/5ef0f060023600ec08c19.jpg",
                         "https://telegra.ph/file/a448465a3a8a251170f76.jpg",
                         "https://telegra.ph/file/eb0ac1557668a98a38cb6.jpg", 
                         "https://telegra.ph/file/fdb3691a17a2c91fbe76c.jpg", 
                         "https://telegra.ph/file/ccdf69ebf6cb85c52a25b.jpg",
                         "https://telegra.ph/file/2adffc55ac0c9733ecc7f.jpg", 
                         "https://telegra.ph/file/faca3b435da33f2f156f1.jpg", 
                         "https://telegra.ph/file/93d0a48c31e16f036f0e8.jpg", 
                         "https://telegra.ph/file/9ed89dc742b172a779312.jpg",
                         "https://telegra.ph/file/0b4c19a19fb834d922d66.jpg", 
                         "https://telegra.ph/file/a95a0deb86f642129b067.jpg", 
                         "https://telegra.ph/file/c4c3d8b5cfc3cc5040833.jpg", 
                         "https://telegra.ph/file/1e1a1b52b9a313e066a04.jpg",
                         "https://telegra.ph/file/a582950a8a259efdcbbc0.jpg",
                         "https://telegra.ph/file/9c3a784d45790b193ca36.jpg", 
                         "https://telegra.ph/file/6aa74b17ae4e7dc46116f.jpg", 
                         "https://telegra.ph/file/e63cf624d1b68a5c819b6.jpg",
                         "https://telegra.ph/file/7e420ad5995952ba1c262.jpg",
                         "https://telegra.ph/file/c7a4dc3d2a9a422c19723.jpg", 
                         "https://telegra.ph/file/163c7eba56fd2e8c266e4.jpg", 
                         "https://telegra.ph/file/5c87b63ae326b5c3cd713.jpg",
                         "https://telegra.ph/file/344ca22b35868c0a7661d.jpg", 
                         "https://telegra.ph/file/a0ef3e56f558f04a876aa.jpg", 
                         "https://telegra.ph/file/217b997ad9b5af8b269d0.jpg", 
                         "https://telegra.ph/file/b3595f99b221c56a5679b.jpg",
                         "https://telegra.ph/file/aba7f4b4485c5aae53c52.jpg", 
                         "https://telegra.ph/file/209ca51dba6c0f1fba85f.jpg", 
                         "https://telegra.ph/file/2a0505ee2630bd6d7acca.jpg", 
                         "https://telegra.ph/file/d193d4191012f4aafd4d2.jpg",
                         "https://telegra.ph/file/47e2d151984bd54a5d947.jpg",
                         "https://telegra.ph/file/2a6c735b47db947b44599.jpg", 
                         "https://telegra.ph/file/7567774412fb76ceba95c.jpg", 
                         "https://telegra.ph/file/6dd8b0edec92b24985e13.jpg",
                         "https://telegra.ph/file/dcf5e16cc344f1c030469.jpg",
                         "https://telegra.ph/file/0718be0bd52a2eb7e36aa.jpg", 
                         "https://telegra.ph/file/0d7fcb82603b5db683890.jpg", 
                         "https://telegra.ph/file/44595caa95717f4db4788.jpg",
                         "https://telegra.ph/file/f3a063d884d0dcde437e3.jpg", 
                         "https://telegra.ph/file/733425275da19cbed0822.jpg", 
                         "https://telegra.ph/file/aff5223e1aa29f212a46a.jpg", 
                         "https://telegra.ph/file/45ccfa3ef878bea9cfc02.jpg",
                         "https://telegra.ph/file/a38aa50d009835177ac16.jpg", 
                         "https://telegra.ph/file/53e25b1b06f411ec051f0.jpg", 
                         "https://telegra.ph/file/96e801400487d0a120715.jpg", 
                         "https://telegra.ph/file/6ae8e799f2acc837e27eb.jpg",
                         "https://telegra.ph/file/265ff1cebbb7042bfb5a7.jpg",
                         "https://telegra.ph/file/4c8c9cd0751eab99600c9.jpg", 
                         "https://telegra.ph/file/1c6a5cd6d82f92c646c0f.jpg", 
                         "https://telegra.ph/file/2c1056c91c8f37fea838a.jpg",
                         "https://telegra.ph/file/f140c121d03dfcaf4e951.jpg", 
                         "https://telegra.ph/file/39f7b5d1d7a3487f6ba69.jpg"
                         ]
@borg.on(admin_cmd(pattern="rpc ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./ravana/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y ")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255,255,255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(60)
        except:
            return
        
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from userbot.utils import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/2eab4f64ead6fbf41bf87.jpg",
                         "https://telegra.ph/file/6bef1ffbaddc5230c2ae1.jpg",
                         "https://telegra.ph/file/a03f035e83098a7c5bded.jpg",
                         "https://telegra.ph/file/f0a230a30b9952f56d2cd.jpg",
                         "https://telegra.ph/file/d00e6bb4b4a483099c992.jpg",
                         "https://telegra.ph/file/1270ed675db61e6c84eea.jpg",
                         "https://telegra.ph/file/32743c9389915b02fdea7.jpg",
                         "https://telegra.ph/file/8c02a1430502bea931ff7.jpg",
                         "https://telegra.ph/file/1ec37d367bb59ac56131d.jpg",
                         "https://telegra.ph/file/e9aeef4fd2e3d0b9e9f24.jpg",
                         "https://telegra.ph/file/28c242ea9f8cf32db4c21.jpg",
                         "https://telegra.ph/file/c089426ca031d1f6297b0.jpg",
                         "https://telegra.ph/file/a196b6c07f0a659daf058.jpg",
                         "https://telegra.ph/file/69f19acd13b1eaf3fc120.jpg"
                        ]
@borg.on(admin_cmd(pattern="survivorpfp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("@Sur_vivor \n \nTime: %H:%M:%S \nDate: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((350, 400), current_time, font=fnt, fill=(230,230,250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(30)
        except:
            return
    
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
         TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/2765633721f6e21a0df9e.jpg",
                        ]
@borg.on(admin_cmd(pattern="epp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("@PerU_MoNster \n \nTime: %H:%M:%S \nDate: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((50, 600), current_time, font=fnt, fill=(230,230,250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(90)
        except:
            return

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [
  "awesome-batman-wallpapers",
  "batman-arkham-knight-4k-wallpaper",
  "batman-hd-wallpapers-1080p",
  "the-joker-hd-wallpaper",
  "dark-knight-joker-wallpaper"
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")
@borg.on(admin_cmd(pattern="batmanpfp ?(.*)"))
async def main(event):
    await event.edit("**Starting batman Profile Pic.**") #Owner @NihiNivi
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(120) #Edit this to your required needs
         except:
            return
