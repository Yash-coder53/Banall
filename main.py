import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

logging.basicConfig(level=logging.INFO)

TOKEN = '8118009991:AAEDlne-l_v8aMkdsB5KDOT8PF9rASBhqjY'

def main():
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    # Handlers
    start_handler = CommandHandler('start', start_callback)
    banall_handler = CommandHandler('banall', banall_callback)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(banall_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
