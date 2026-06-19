from aiogram import types
from handlers.keyboards import main_keyboard 

async def help_button(message: types.Message):
    await message.answer(
        "Выберите исследование с помощью кнопок ниже 👇\n\n⚠️ Бот не заменяет визит к врачу.", 
        reply_markup=main_keyboard
    )

async def handle_other(message: types.Message):
    await message.answer(
        "Пожалуйста, выберите исследование из меню 👇\n\n⚠️ Бот не заменяет визит к врачу.", 
        reply_markup=main_keyboard
    )