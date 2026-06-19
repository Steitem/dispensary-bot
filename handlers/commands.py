from aiogram import types
from handlers.keyboards import main_keyboard

async def cmd_start(message: types.Message):
    await message.answer(
        "👋 <b>Привет!</b>\n\n"
        "Я — Ассистент диспансера.\n"
        "Помогу правильно подготовиться к диагностике.\n\n"
        "Выберите нужное исследование 👇",
        parse_mode="HTML",
        reply_markup=main_keyboard
    )

async def cmd_help(message: types.Message):
    await message.answer("📋 Используйте кнопки ниже или команду /start")

async def go_back(message: types.Message):
    await message.answer(
        "👋 <b>Главное меню</b>\n\n"
        "Выберите нужное исследование 👇",
        parse_mode="HTML",
        reply_markup=main_keyboard
    )