from aiogram import types
from config import dp,bot
from Include.core.helpers import telegram as tg_helper
from Include.core.helpers.requestApi import *
from aiogram.dispatcher import FSMContext
from .messages import *
from Include.core.states import Answer

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("answertask"),state="*")
async def answer(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['test'] = callback_query.data
        await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                                      reply_markup=None)
        await bot.send_message(callback_query.from_user.id,"Введите ответ")
        await Answer.WriteAns.set()



@dp.message_handler(lambda message: message.text, state=Answer.WriteAns,content_types=types.ContentTypes.TEXT)
async def writeanss(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        id_que = str(data['test']).split("_")[1]
        count = str(data['test']).split("_")[2]
        tgid = str(data['test']).split("_")[3]
        task_id = str(data['test']).split("_")[4]
        data = complete_question(id_que,message.text)
        if "correct" in data:
            await bot.send_message(message.from_user.id, "Ответ не правильный. Повтори тему по сыллке\n"+get_task(task_id)['link_theme'])
        else:
            await bot.send_message(message.from_user.id, get_task(task_id)['feedback'])
        await state.finish()

async def send_questions_for_all_users():
    users = get_users()
    for user in users:
        tgid = user['telegram_id']
        question = get_question(tgid)
        task = get_task(question['task_id'])
        id_que = question['id']
        btn = [('Ответить на вопрос','answertask_'+str(id_que)+"_"+str(1)+"_"+str(tgid)+"_"+str(question['task_id']))]
        finish_btns = tg_helper.create_inline_markup(*btn)
        await bot.send_message(chat_id=tgid,text="Tема: "+task['theme']+"\nЗадание: "+task['question'],reply_markup=finish_btns)