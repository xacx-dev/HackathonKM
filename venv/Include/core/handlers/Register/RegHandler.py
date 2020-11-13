from aiogram import types
from config import dp,bot
from .messages import *

@dp.callback_query_handler(text='no_reg',state="*")
async def process_callback_regno(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, no_start_msg)
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(text='yes_reg',state="*")
async def process_callback_regyes(callback_query: types.CallbackQuery):
    await bot.send_photo(chat_id=callback_query.from_user.id,photo='AgACAgIAAxkBAAMKX66FpHbeK80mQVaAL9m6kCoyJ98AAlCwMRv0xHBJtYgnezSLjfflcWiXLgADAQADAgADeAAD6g4DAAEeBA',
                         caption='ПОЕХАЛИ!!!\n\n')
    await bot.answer_callback_query(callback_query.id)
