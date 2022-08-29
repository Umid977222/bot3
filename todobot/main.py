from aiogram import Bot, Dispatcher, executor, types
from config import token
from aiogram.dispatcher import FSMContext
import logging
from aiogram.dispatcher.filters import CommandStart

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode="html")
dp = Dispatcher(bot=bot)


@dp.message_handler(CommandStart())
async def on_start(message: types.Message):
    await message.reply(
        text=f"Hi bot {message.from_user.full_name}"
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)

