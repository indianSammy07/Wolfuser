"""Check if userbot alive or not . """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME 
from userbot.utils import admin_cmd,sudo_cmd
from telethon import version
from platform import python_version, uname

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "WolfUserbot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**Telethon Userbot powered by**\n\n"
                     "💻*Status*:`online`\n
                     f"🌐*Telethon*: {version.__version__}\n`"
                     f"🐍*Python*: {python_version()}\n`"
                     "🐺*Owner*:[WolfUserbot](https://GitHub.come/indianSammy07/WolfUserbot)"
                     "🤖*Userbot name*:`wolfuserbot\n`"
                     "*The power of imagination make me infinity*\n"
                     "🗳️*Plugin*:`God Know`\n"
                     "⛑️*Repo Status*:[public](https://telegra.ph/file/92b4a6fc9f5d7de83b98b.jpg)"
                     f"`☞My peru owner`: [{DEFAULTUSER}](@rkprojects)\n"
                     #"[Deploy this userbot Now](https://github.com/indianSammy07/WolfUserbot)"
                    )
    
    


@borg.on(sudo_cmd(pattern="sudo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.reply("YOU ARE SUDO FOR THIS BOT \n\n"
                     f"☞Telethon version: {version.__version__}\n"
                     f"☞Python: {python_version()}\n"
                     f"☞My peru owner: {DEFAULTUSER}\n"
                     #"Deploy this userbot Now"
                    )
       
CMD_HELP.update({"alive": "`.alive` :\
      \nUSAGE: Type .alive to see wether your bot is working or not. "
}) 
