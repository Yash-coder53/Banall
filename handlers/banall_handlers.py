def banall_callback(update, context):
    # Implement your banall logic here
    context.bot.send_message(chat_id=update.effective_chat.id, text='Banall command received!')
