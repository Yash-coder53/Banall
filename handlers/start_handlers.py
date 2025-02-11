def start_callback(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to Banall Telegram Bot!')
