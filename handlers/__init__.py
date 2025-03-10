from Slayer.ban_all import ban_all_handler
from Slayer.start import start_handler
from Slayer.help import help_handler

Register all handlers here
handlers = [
    CommandHandler('/banall',ban_all_handler),
    CommandHandler('/start',start_handler),
    CommandHandler('/help',help_handler) 
]
