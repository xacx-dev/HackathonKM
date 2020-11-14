from aiogram import types
from config import dp,bot
from Include.core.helpers import telegram as tg_helper
from Include.core.helpers.requestApi import *
from Include.core.handlers.Profile.messages import get_info_user
from .messages import *


@dp.message_handler(lambda message: message.text and 'база пользователей' in message.text.lower())
async def profile_info(message: types.Message):
    tgid = message.from_user.id
    data = get_info_user(get_users()[0]['telegram_id'])
    await bot.send_message(chat_id=message.from_user.id,text=base_users_text+"\n"+data,reply_markup=bnts_users(get_users(),0,tgid))



@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("gonext"))
async def goback(callback_query: types.CallbackQuery):
    id = str(callback_query.data).split("_")[1]
    tgid = callback_query.from_user.id
    users =get_users()
    data = get_info_user(users[int(id)]['telegram_id'])
    await bot.edit_message_text(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                           text=base_users_text + "\n" + data,
                           reply_markup=bnts_users(users, id,tgid))
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("goback"))
async def goback(callback_query: types.CallbackQuery):
    id = str(callback_query.data).split("_")[1]
    tgid = callback_query.from_user.id
    users =get_users()
    data = get_info_user(users[int(id)]['telegram_id'])
    await bot.edit_message_text(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                           text=base_users_text + "\n" + data,
                           reply_markup=bnts_users(users, id,tgid))
    await bot.answer_callback_query(callback_query.id)



def bnts_users(users,id,tgid):
    btns = []
    id = int(id)

    if len(users)>1 and id == 0:
        btns.append(("Вперед", "gonext_"+str(id+1)))
    elif len(users) != (id+1):
        btns.append(("Вперед", "gonext_"+str(id+1)))
        btns.append(("Назад", "goback_"+str(id-1)))
    elif len(users) == (id+1):
        btns.append(("Назад", "goback_" + str(id - 1)))

   # if users[id]['telegram_id'] != tgid:
   #     btns.append(("Предложить общаться", "gochat_"+tgid+"_"+id))
    finish_btns = tg_helper.create_inline_markup(*btns, row_width=2)
    return finish_btns