import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserNotParticipant
from plugins.forcesub import ForceSub
@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
await ForceSub(bot, update)
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )
