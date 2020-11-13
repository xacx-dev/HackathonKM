from aiogram import types
from config import dp
from .messages import *

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(start_msg,reply_markup=start_btn)