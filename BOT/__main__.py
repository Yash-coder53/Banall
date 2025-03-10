from Slayer import idle
from Slayer.config import Config
from Slayer import bot, ass
bot.start()
if Config.PYRO_SESSION:
   ass.start()
idle()
bot.stop()
