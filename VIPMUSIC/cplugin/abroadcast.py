import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import AUTO_GCAST, AUTO_GCAST_MSG
from VIPMUSIC import app
from VIPMUSIC.utils.database import get_served_chats_clone

# Convert AUTO_GCAST to boolean based on "On" or "Off"
AUTO_GCASTS = AUTO_GCAST.strip().lower() == "on"

START_IMG_URLS = "https://telegra.ph/file/9448f15c5b9debd6b5646.jpg"

MESSAGES = f"""**🌹𝖧𝖾𝗅𝗅𝗈 𝖥𝗋𝗂𝖾𝗇𝖽𝗌 𝖠𝗋𝖾 𝖸𝗈𝗎 𝖫𝗈𝗈𝗄𝗂𝗇𝗀 𝖥𝗈𝗋 𝖺 𝖢𝗁𝖺𝗍𝗍𝗂𝗇𝗀 𝖦𝗋𝗈𝗎𝗉..??

🌙 𝖧𝖾𝗋𝖾 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖬𝖾𝖾𝗍 𝖭𝖾𝗐 𝖯𝖾𝗈𝗉𝗅𝖾 𝖺𝗌 𝗐𝖾𝗅𝗅 𝖺𝗌 :-
       𝟐𝟒 𝐱 𝟕 𝖢𝗁𝖺𝗍𝗍𝗂𝗇𝗀 💸
       𝖬𝖺𝗄𝖾 𝖭𝖾𝗐 𝖥𝗋𝗂𝖾𝗇𝖽s 🐝
       𝖤𝗇𝗃𝗈𝗒 𝖵𝖼/𝖲𝗈𝗇𝗀𝗌 🥂
       

𝖩𝗈𝗂𝗇 𝖮𝗎𝗋 𝖢𝗁𝖺𝗍𝗍𝗂𝗇𝗀 𝖦𝗋𝗈𝗎𝗉 :
https://t.me/+0oLx7Rvk_EU1MDNl

https://t.me/+0oLx7Rvk_EU1MDNl

https://t.me/+0oLx7Rvk_EU1MDNl **"""
BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ Click  ๏",
                url=f"https://telegram.me/ab_krishna_uff",
            )
        ]
    ]
)

MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs + ᴄʜᴀɴɴᴇʟs ᴠᴄ. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟᴜʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... ❤️

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏",
                url=f"https://t.me/Friendship143_Robot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴɢ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ.**\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (Off)]**"""


async def send_message_to_chats(client: Client, message: Message):
    try:
        chats = await get_served_chats_clone()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):
                try:
                    await client.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTONS,
                    )
                    await asyncio.sleep(20)
                except Exception as e:
                    pass
    except Exception as e:
        pass


async def continuous():
    while True:
        if AUTO_GCASTS:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass
        await asyncio.sleep(100000)


if AUTO_GCASTS:
    asyncio.create_task(continuous())
