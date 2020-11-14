from aiogram import types
from config import dp,bot
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from Include.core.states import Register
from Include.core.helpers.requestApi import *
from .messages import *

@dp.callback_query_handler(text='no_reg',state="*")
async def process_callback_regno(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, no_start_msg)
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(text='yes_reg',state="*")
async def process_callback_regyes(callback_query: types.CallbackQuery):
    users = get_users()
    for id in range(0, len(users)):
        tgid = users[id]['telegram_id']
        if tgid == callback_query.from_user.id:
            await bot.send_message(callback_query.from_user.id,reg_already_finished)
            await bot.answer_callback_query(callback_query.id)
            return
    await bot.send_photo(chat_id=callback_query.from_user.id,photo='AgACAgIAAxkBAAMKX66FpHbeK80mQVaAL9m6kCoyJ98AAlCwMRv0xHBJtYgnezSLjfflcWiXLgADAQADAgADeAAD6g4DAAEeBA',
                         caption='ПОЕХАЛИ!!!\n\n'+first_name_txt)
    await bot.answer_callback_query(callback_query.id)
    await Register.FirstName.set()


@dp.message_handler(lambda message: message.text, state=Register.FirstName,content_types=types.ContentTypes.TEXT)
async def first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        message.text = str(message.text).lower().title()
        data['fname'] = message.text
        await bot.send_message(message.from_user.id, last_name_txt)
        await Register.next()

@dp.message_handler(lambda message: message.text, state=Register.LastName,content_types=types.ContentTypes.TEXT)
async def last_namef(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        message.text = str(message.text).lower().title()
        data['lname'] = message.text
        await bot.send_message(message.from_user.id, university_txt)
        await Register.next()

@dp.message_handler(lambda message: message.text, state=Register.University,content_types=types.ContentTypes.TEXT)
async def univerf(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        message.text = str(message.text).lower().title()
        if message.text == "0":
            data['univer'] = ""
        else:
            data['univer'] = message.text
        await bot.send_message(message.from_user.id, email_text)
        await Register.next()

@dp.message_handler(lambda message: message.text, state=Register.Email,content_types=types.ContentTypes.TEXT)
async def emailf(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        message.text = str(message.text).lower().title()
        if message.text == "0":
            data['email'] = ""
        else:
            data['email'] = message.text
        await bot.send_message(message.from_user.id, vk_text)
        await Register.next()

@dp.message_handler(lambda message: message.text, state=Register.Vk,content_types=types.ContentTypes.TEXT)
async def VKf(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        message.text = str(message.text).lower().title()
        if message.text == "0":
            data['vk'] = ""
        else:
            data['vk'] = message.text
        await bot.send_message(message.from_user.id, about_you)
        await Register.next()

@dp.message_handler(lambda message: message.text, state=Register.About_me,content_types=types.ContentTypes.TEXT)
async def about_finishf(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        message.text = str(message.text).lower().title()
        if message.text == "0":
            data['about'] = ""
        else:
            data['about'] = message.text
        reguser(data,message.from_user.id)

        profile = KeyboardButton('Информация о профиле')
        base = KeyboardButton('База пользователей')
        btns = ReplyKeyboardMarkup(resize_keyboard=True)
        btns.add(profile,base)
        await bot.send_message(chat_id=message.from_user.id, text=reg_finished, reply_markup=btns)
        await state.finish()

def reguser(data,tgid):
    data = {
        "telegram_id": tgid,
        "first_name": data['fname'],
        "last_name": data['lname'],
        "university": data['univer'],
        "email": data['email'],
        "vk": data['vk'],
        "about_me": data['about']
            }
    create_user(data)






