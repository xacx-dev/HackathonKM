from aiogram import executor
from loguru import logger
from config import bot,dp
import core.handlers
import core.helpers
import asyncio
import time
from Include.core.helpers.requestApi import *
from Include.core.handlers.TestingSystem.TestingHandler import send_questions_for_all_users


async def send_questions():
    statuses = get_statuses()
    for i in statuses:
        if i['status'] == "string":
            await send_questions_for_all_users()
            edit_status(i['id'], "1")
    print("Questions sended")


async def update_questions():
    init_tasks()
    time.sleep(5)
    get_init_question()
    get_init_settings()
    print("BD is updated")


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)


if __name__ == '__main__':
    DELAY = 15
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, update_questions, loop)
    loop.call_later(DELAY, repeat, send_questions, loop)
    executor.start_polling(dp, skip_updates=True)








