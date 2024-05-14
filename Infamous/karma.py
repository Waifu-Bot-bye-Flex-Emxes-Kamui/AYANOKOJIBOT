# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/09ab378427656bbbd8dd2.png",
    "https://telegra.ph/file/f6579bf084c0727786bea.png",
    "https://telegra.ph/file/cef947b748551d6f8e9d5.png",
    "https://telegra.ph/file/4b0fb874f97473332afbd.png",
    "https://telegra.ph/file/ddca302dd6657f45deaf0.png",
    "https://telegra.ph/file/1a5e0d1100bb744da8dfe.png",
    "https://telegra.ph/file/49b5ce2505f58d89d1a21.png",
]

HEY_IMG = "https://telegra.ph/file/56d52ef4d9d395f6e72ca.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/77f63d46852e71e6ed253.mp4",
    "https://telegra.ph/file/c58216956c10072f41a7e.mp4",
    "https://telegra.ph/file/c56c19b62908e7049bcce.mp4",
    "https://telegra.ph/file/3a213a4b123968c573b06.mp4",
    "https://telegra.ph/file/6c403721c68be4cacbb6e.mp4",
    "https://telegra.ph/file/e928293fb60fe13c653ec.mp4",
    "https://graph.org/file/b4943d2c681b5f3e31dab.mp4",
    "https://telegra.ph/file/3a213a4b123968c573b06.mp4",
]

BAN_GIFS = [
    "https://graph.org/file/efde2d79b2c7dd5a22eee.mp4",
]


KICK_GIFS = [
    "https://graph.org/file/1ea4fc87bf99933fb3af7.mp4",
]


MUTE_GIFS = [
    "https://graph.org/file/7b91b74f66d073aa6e263.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ᴋɪʏᴏᴛᴀᴋᴀ, ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Hydra_Updates"),
        ib(text="SUPPORT", url="https://t.me/hydraXsupport"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
