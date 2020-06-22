"""Check if userbot alive or not . """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME 
from userbot.utils import admin_cmd,sudo_cmd
from telethon import version
from platform import python_version, uname

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**MY BOT IS RUNNING SUCCESFULLY**\n\n"
                     f"☞**Telethon Version:** {version.__version__}\n"
                     f"☞**Python: **{python_version()}\n"
                     f"☞**Database Status: **Databases functioning normally!\n"
                     f"☞Always with you, my Master! Try `.help` for more information!!\n"
                     f"☞My peru owner: {DEFAULTUSER}\n\n"
                      "[Deploy Catuserbot Now](https://github.com/sandy1709/catuserbot)"
                    )
    
@borg.on(sudo_cmd(pattern="sudo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.reply("YOU ARE SUDO FOR THIS BOT \n\n"
                     f"☞Telethon version: {version.__version__}\n"
                     f"☞Python: {python_version()}\n"
                     f"☞My peru owner: {DEFAULTUSER}\n"
                     f"Send `.help` for commands"
                     #"Deploy this userbot Now"
                    )
       
CMD_HELP.update({"alive": "`.alive` :\
      \nUSAGE: Type .alive to see wether your bot is working or not. "
}) 
