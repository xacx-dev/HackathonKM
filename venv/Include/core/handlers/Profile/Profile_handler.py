from aiogram import types
from config import dp,bot
from .messages import *

@dp.message_handler(lambda message: message.text and 'информация о профиле' in message.text.lower())
async def profile_info(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,text=profile_security
                                                             +"\n"+get_info_user(message.from_user.id))
