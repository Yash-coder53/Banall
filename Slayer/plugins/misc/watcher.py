from Slayer import filters
from Slayer.types import Message

from Slayer import app
from Slayer.core.call import Anony

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Anony.stop_stream_force(message.chat.id)
