from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import json

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
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

# Этот хэндлер будет срабатывать на отправку фото
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

# Этот хэндлер будет срабатывать на отправку видео
async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)

# Этот хэндлер будет срабатывать на отправку видео сообщений
async def send_video_note_echo(message: Message):
    await message.reply_video_note(message.video_note.file_id)

# Этот хэндлер будет срабатывать на отправку стикеров
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)

# Этот хэндлер будет срабатывать на отправку аудио файлов
async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)

# Этот хэндлер будет срабатывать на отправку голосовых сообщений
async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)

# Этот хэндлер будет срабатывать на отправку любых файлов
async def send_files(message: Message):
    await message.reply_document(message.document.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)

# print(json.dumps(message.model_dump(), indent=4))
# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_video_note_echo, F.video_note)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_files,F.document)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)