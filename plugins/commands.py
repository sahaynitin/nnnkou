import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserNotParticipant
from database.adduser import Adduser #from plugins.forcesub import ForceSub
from plugins.forcesub import ForceSub

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
        #reply_markup=Translation.START_BUTTONS#
