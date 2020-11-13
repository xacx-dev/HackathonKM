from typing import List
from aiogram import types

def create_inline_markup(*btns_data: tuple, row_width=2) -> types.InlineKeyboardMarkup:
    btns = []
    for text, callback in btns_data:
        if str(callback).__contains__("http"):
            data = {
                "text": text,
                "url": callback
            }
            btns.append(data)
        else:
            data = {
                "text": text,
                "callback_data": callback
            }
            btns.append(data)

    btns = btns
    keyboard_markup = types.InlineKeyboardMarkup(row_width=row_width)
    keyboard_markup.add(*btns)
    return keyboard_markup