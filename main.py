# from pytube import Playlist
from pytube import Playlist,YouTube
from pprint import pprint
from pytube.exceptions import VideoUnavailable
import time
from config import bot_token
import re
pattern = r'^https?:\/\/(?:www\.)?youtube\.com\/playlist\?list=[\w-]+(?:&[\w-]+(=[\w-]*)?)*$'
from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import (CommandHandler,
                          CallbackContext,
                          ContextTypes,
                          Application,
                          CommandHandler,
                          MessageHandler,
                          filters)

from database import addUser,totalUsers
from keyboard import DEV_MARKUP
async def start(update: Update,context:ContextTypes.DEFAULT_TYPE) -> None:
    
        await update.message.reply_text(text="<b>welcome just send me the playlist link i will send you the links of each video in <code>MONOSPACED</code></b>\n<b>NOTE: THIS BOT IS CURRENTLY IN BETA VERSION</b> ",reply_to_message_id=update.message.message_id,allow_sending_without_reply=True,parse_mode=ParseMode.HTML,reply_markup=DEV_MARKUP)
        user_id = update.effective_user.id
        first_name = update.effective_user.first_name
        last_name = update.effective_user.last_name
        user_name = update.effective_user.username
        addUser(user_id, first_name, last_name, user_name)

async def link_extractor(update:Update,context:CallbackContext) -> None:
    result = re.match(pattern=pattern,string=update.message.text)
    if result==None:
        await update.message.reply_text(text=f"not a valid playlist link ", reply_to_message_id=update.message.id, allow_sending_without_reply=True)
        return
    await update.message.reply_text(text=f"link extraction started....", reply_to_message_id=update.message.id, allow_sending_without_reply=True)
    playlist_link = update.message.text
    playlist = Playlist(playlist_link)
    i = 0
    for url in playlist.video_urls:
        i +=1 
        try :
            yt = YouTube(url)
        except VideoUnavailable:
            await update.message.reply_text(text=f"{i}.skipping this video due to unavailbility {url}", reply_to_message_id=update.message.id, allow_sending_without_reply=True)
            continue
        finally:
            title = yt.title
            thumbnail = yt.thumbnail_url
            await update.message.reply_photo(photo= thumbnail, 
                               caption=f"{i}.<b>{title}</b> \n<b>link:</b><code>{url}</code>", reply_to_message_id=update.message.id, allow_sending_without_reply=True,
                               parse_mode=ParseMode.HTML)
            


def main():

    application = Application.builder().token(
        bot_token).build()
    application.add_handler(CommandHandler('start',start))
    application.add_handler(MessageHandler(filters=filters.TEXT & ~filters.COMMAND,callback=link_extractor))
    application.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == '__main__':
    main()

