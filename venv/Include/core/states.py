from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



class Register(StatesGroup):
    FirstName = State()
    LastName = State()
    University = State()
    Email = State()
    Vk = State()
    About_me = State()

class Answer(StatesGroup):
    WriteAns = State()
