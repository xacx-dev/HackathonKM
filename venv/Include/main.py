from aiogram import executor
from loguru import logger
from config import *
import core.handlers
import core.helpers
from threading import Thread
import time
from Include.core.helpers.requestApi import *


def init_tasksf():
    while True:
        init_tasks()
        time.sleep(5)
        get_init_question()
        get_init_settings()
        print("BD is updated")
        time.sleep(600)





if __name__ == "__main__":
    Thread(target=init_tasksf).start()
    executor.start_polling(dp, skip_updates=True)

