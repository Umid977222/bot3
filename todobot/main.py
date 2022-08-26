from aiogram import Bot, Dispatcher, executor, types
from config import token
from aiogram.dispatcher import FSMContext
import logging

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode="html")
dp = Dispatcher(bot=bot)