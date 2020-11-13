from aiogram import types
from core.helpers import telegram as tg_helper



start_msg = 'Готов ли ты окунуться в мир новых знаний вместе со мной?'
start = [
    ("Хочу всё знать!", "yes_reg"),
    ("Я уже знаю.", "no_reg")
]


start_btn = tg_helper.create_inline_markup(*start)
