from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import os
from dotenv import load_dotenv
# Загружаем переменные из .env файла
load_dotenv()
# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def get_pizza_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍕 Маргарита", callback_data="pizza_margarita")],
        [InlineKeyboardButton(text="🍕 Пепперони", callback_data="pizza_pepperoni")],
        [InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm")]
    ])

@dp.message(Command("pizza"))
async def pizza_command(message: types.Message):
    await message.answer("Выберите пиццу:", reply_markup=get_pizza_keyboard())

selected_pizza = None

@dp.callback_query()
async def handle_pizza_selection(callback: types.CallbackQuery):
    global selected_pizza

    if callback.data.startswith("pizza_"):
        selected_pizza = callback.data.split('_')[1]
        await callback.answer(f"Выбрана: {selected_pizza}")
    elif callback.data == "confirm":
        if selected_pizza:
            await callback.message.edit_text(
                f"✅ Заказ подтвержден: {selected_pizza}",
                reply_markup=None
            )
            await callback.answer("Заказ принят!")
        else:
            await callback.answer("Сначала выберите пиццу!", show_alert=True)

if __name__ == "__main__":
    dp.run_polling(bot)