"""Check if userbot alive or not . """
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
  CAT_IMG = "https://telegra.ph/file/a6c81b071ebe187d051c1.jpg"
else:
  CAT_IMG = ALIVE_PIC


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@MrSemmy"

cat_caption = "**𝕄𝕪 𝕓𝕠𝕥 𝕚𝕤 𝕣𝕦𝕟𝕟𝕚𝕟𝕘 𝕤𝕦𝕔𝕔𝕖𝕤𝕤𝕗𝕦𝕝𝕝𝕪**\n\n"
cat_caption += f"🛡"😒𝔸ℙ𝕌ℕ 𝕀𝔻ℍ𝔸ℝ𝕀ℂℍ ℍ𝔸𝕀😒\n\n"
cat_caption += f"🛡"♥️тєℓєтнση νєяѕιση: {version.__version__}\n\n"
cat_caption += f"🛡"🐺ρутнση νєяѕιση: {python_version()}\n\n"
cat_caption += "🛡**Always With You, My Master!**\n\n"
cat_caption += f"🛡"🤘вσт νєяѕιση:` 🐺 WolfUserbot\n\n"
cat_caption += "🛡"⚙️мαιηтαιηєя: [𝕎𝕠𝕝𝕗𝔾𝕒𝕟𝕘](t.me/rkprojects)\n\n"
cat_caption += "🛡"====================================\n\n"
cat_caption += "🛡"👦🏻υѕєя: {DEFAULTUSER}\n\n"
cat_caption += "**[⚜️🅳🅴🅿🅻🅾🆈⚜️](https://github.com/indianSammy07/WolfUserbot)**"
cat_caption += f"====================================\n\n")


@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete()
    await borg.send_file(alive.chat_id, CAT_IMG, caption=cat_caption)
