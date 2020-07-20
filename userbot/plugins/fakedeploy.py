"""Emoji

Available Commands:

.deploy"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern=r"deploy"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

   # input_str = event.pattern_match.group(1)



    await event.edit("Typing...")

    animation_chars = [
        
            "**Heroku Connecting To Latest Github Build (WolfUserbot)**",
            "**Build started by user**",
            "**Deploy** `535a74f0` **by user** ",
            "**Restarting Heroku Server...**",
            "**State changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m userbot`",
            "**State changed from starting to up**",
            "__INFO:WolfUserbot:Logged in.__",
            "__INFO:WolfUserbot:Successfully loaded all plugins__",
            "**Build Succeeded**"

 ]

    for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
