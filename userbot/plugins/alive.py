"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @Nitesh_231
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
PM_IMG = "https://telegra.ph/file/92b4a6fc9f5d7de83b98b.jpg"
pm_caption = "`Wolf iS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**Wolf OS** : `3.14`\n"
pm_caption += "**Current Sat** : `WolfGangSat-2.25`\n\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n\n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "**License** : [MIT Licence](github.com/indianSammy07/WolfUserbot/blob/master/LICENSE)\n"
pm_caption += "Copyright : By [indianSammy07@Github](GitHub.com/indianSammy07)\n"
pm_caption += "[Deploy WolfUserbot](https://t.me/RkProjects/13)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
