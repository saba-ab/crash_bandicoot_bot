from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot_token = '6308617577:AAFr1PVp0SQSfMv5keYXK172FOcD0ANGvZk'
storage = MemoryStorage()


bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=storage)
