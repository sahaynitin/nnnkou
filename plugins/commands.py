import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserNotParticipant
from helper_funcs.forcesub import ForceSub

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    await update.reply_text(
        text=Translation.HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=Translation.HELP_BUTTONS
    )

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    await update.reply_text(
        text=Translation.ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=Translation.ABOUT_BUTTONS
    )
@Client.on_callback_query(filters.regex('^refreshmeh$'))
async def refreshmeh_cb(bot, message):
    if Config.UPDATES_CHANNEL:
        invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
        try:
            user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), message.from_user.id)
            if user.status == "kicked":
                await message.message.edit(
                    text="Sorry Sir, You are Banned. Contact My [Support Group](https://t.me/tellybots_support).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await message.message.edit(
                text="**You Still Didn't Join ☹️, Please Join My Updates Channel To Use Me!**\n\nDue to Overload, Only Channel Subscribers Can Use Me!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=invite_link.invite_link)
                        ],
                        [
                            InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await message.message.edit(
                text="Something Went Wrong. Contact My [Support Group](https://t.me/SDBOTz).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    await message.answer()
    await start(bot, message, True)
