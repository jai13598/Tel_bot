import logging
from telegram import Update
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackContext
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' , level=logging.INFO)
logger=logging.getLogger(__name__)

TOKEN= ""

def start(bot,update):
	print(update)
	author=update.message.from_user.first_name
	reply="Hi {} ! My name is SuperBot ".format(author)
	bot.send_message(chat_id=update.message.chat_id,text=reply)
def _help(bot,update):
	help_text="Hey ! This is a help text."
	bot.send_message(chat_id=update.message.chat_id,text=help_text)

def echo_text(bot,update):
	reply=update.message.text
	bot.send_message(chat_id=update.message.chat_id,text=reply)
def echo_sticker(bot,update):
	bot.send_stricker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)
	
def error(bot,update):
	logger.error("Update '%s' coused error '%s' ",update,update.error)

def main():
	updater=Updater(TOKEN)
	dp=updater.dispatcher
	dp.add_handler(CommandHandler("start",start))
	dp.add_handler(CommandHandler("help",_help))
	dp.add_handler(MessageHandler(Filters.text,echo_text))
	dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
	dp.add_error_handler(error)	

	updater.start_polling()
	logger.info("start_polling...")
	updater.idle()


if __name__ == '__main__':
	main()
