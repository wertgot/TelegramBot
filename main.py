from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(lambda msg: msg.text and msg.text == "/start")
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')

# print(message.model_dump_json(indent=4, exclude_none=True))

if __name__ == '__main__':
    dp.run_polling(bot)