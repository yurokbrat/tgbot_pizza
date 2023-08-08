from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bott = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bott, storage=storage)
