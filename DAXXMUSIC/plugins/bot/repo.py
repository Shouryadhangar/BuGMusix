from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
♡︎ ωεℓ¢σмє ƒσя ˹ʙʊɢ ✘ ʙᴏᴛs ˼ ♡︎
 
 ✯ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✯
 
 ✯ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✯
 
 ✯ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✯
 
 ✯ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✯
 
 ✯ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✯
 
 ✯ ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝐊ɪᴅɴᴀᴘ 𝐌ᴇ ❤️‍🩹🍃", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("❥︎ Gʀᴏᴜᴘ 1 💗🍃", url="https://t.me/+GwJYO4nhgWU5NDhl"),
          InlineKeyboardButton("❥︎ Gʀᴏᴜᴘ 2 💗🍃", url="https://t.me/BuG_x_Support"),
          ],
[
          InlineKeyboardButton("💗 ᴄʜᴀɴɴᴇʟ 💗", url="https://t.me/xD_Feelings"),
          InlineKeyboardButton("💗 ᴅᴘᴢ ᴄʜᴀɴɴᴇʟ 💗", url="https://t.me/Unconditional_Dps"),
          ],
[
              InlineKeyboardButton("˹ʙʊɢ ✘ ɢᴀϻᴇ ˼ 💗", url=f"https://t.me/BuG_x_GameBot"),
              InlineKeyboardButton("︎˹ʙʊɢ ✘ ʀᴀɴᴋɪɴɢs ˼ 💗", url=f"https://t.me/BuG_RaNk_Bot"),
              ],
[
InlineKeyboardButton("𝐎ᴡɴᴇʀ ♕︎", url=f"https://t.me/NoT_uR_SoHeL"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/0b1903362f0a70885c091.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://github.com/SH251204/BuGMusix/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/SH251204/BuGMusix) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/+EKbRf8cIsIo3NTVl)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


