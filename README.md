# ELIZA
##rewrited by @peru_monster

This is a userbot made for telegram. I made this userbot with help of all other userbots available in telegram. All credits goes to its Respective Owners...
# For any query:-
### [Join Here For Any Query](https://t.me/Eliza_userbot_support)

### The Easy Way to deploy the bot
Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Generate stringsession by clicking on run.on.repl.it button below and then click on deploy to heroku . Before clicking on deploy to heroku just click on fork and star just below


[![Get string session](https://repl.it/badge/github/PerU-MoNsteR/Eliza)](https://repl.it/@SuhaashL/generatestring#main.py)


[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PerU-MoNsteR/Eliza/tree/master)


<p align="center">
  <a href="https://github.com/PerU-MoNsteR/Eliza/fork">
    <img src="https://img.shields.io/github/forks/PerU-MoNsteR/Eliza?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/PerU-MoNsteR/Eliza">
    <img src="https://img.shields.io/github/stars/PerU-MoNsteR/Eliza?style=social">
  </a>
</p>

[![Elizalogo](https://telegra.ph/file/ced30b3600c5a4e6b2d8a.jpg)](https://heroku.com/deploy?template=https://github.com/PerU-MoNsteR/Eliza)

## The Normal Way
Simply clone the repository and run the main file:
```sh
git clone https://github.com/PerU-MoNsteR/Eliza
cd eliza
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```
An example `local_config.py` file could be:
**Not All of the variables are mandatory**
__The Userbot should work by setting only the first two variables__
```python3
from heroku_config import Var
class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```
### uniborg Configuration

The uniborg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the uniborg Support Config.

