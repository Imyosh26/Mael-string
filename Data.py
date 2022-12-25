from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴀʟʟᴏ {}

sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ {}

ʙᴏᴛ ɪɴɪ ᴀᴍᴀɴ ᴅᴀɴ ᴛᴇʀᴘᴇʀᴄᴀʏᴀ, sɪsᴛᴇᴍ ᴋᴇʀᴊᴀ ʙᴏᴛ ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇɴɢᴀᴍʙɪʟᴀɴ sᴛʀɪɴɢ sᴇᴀssɪᴏɴ ᴅᴀɴ ʟᴀɴɢsᴜɴɢ ᴅɪ ᴋɪʀɪᴍ ᴋᴇ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ

ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ʙʏ : @itsdaps

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ", url="https://t.me/projectdaps")],
        [
            InlineKeyboardButton("ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ ❔", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴғᴏ ʙᴏᴛ ʟᴀɪɴ", url="https://t.me/privatedap")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @HiroshiXbot

Group Support : [ɢᴀʙᴜɴɢ ᴋᴏɴᴛᴏʟ](https://t.me/hirt)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @itsdaps
    """
