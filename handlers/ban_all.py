from Slayer.ext import CommandHandler
def ban_all_handler(update,context):
  context.bot.send_message(chat_id=update.effective_chat.id,text="Banning started")
