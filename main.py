import asyncio
import sqlite3
import re
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F

from config import TOKEN

# Импорты handlers
from handlers.commands import cmd_start, cmd_help, go_back
from handlers.blood import blood_analysis
from handlers.uzi import uzi
from handlers.fgds import fgds
from handlers.mrt import mrt
from handlers.kt import kt
from handlers.xray import xray
from handlers.ecg import ecg
from handlers.faq_home import faq_home
from handlers.faq_callback import router as faq_router

# Импорт админ-функций
from admin_handlers import (
    admin_panel,
    set_avatar,
    set_name,
    set_description,
    get_stats,
    broadcast
)

# Импорты новых клавиатур
from inline_keyboards import (
    main_menu_keyboard,
    research_keyboard,
    back_keyboard,
    back_to_research_keyboard,
    research_done_keyboard,
    cancel_question_keyboard
)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хранилище состояний пользователей
user_question_mode = {}

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('state.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_states (
            chat_id INTEGER PRIMARY KEY,
            last_research TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Функция для сохранения состояния
def save_user_state(chat_id, research_type):
    conn = sqlite3.connect('state.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO user_states (chat_id, last_research)
        VALUES (?, ?)
    ''', (chat_id, research_type))
    conn.commit()
    conn.close()

def get_user_state(chat_id):
    conn = sqlite3.connect('state.db')
    cursor = conn.cursor()
    cursor.execute('SELECT last_research FROM user_states WHERE chat_id = ?', (chat_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Функция для проверки текста
def is_valid_text(text):
    pattern = r'^[а-яА-Яa-zA-Z0-9\s\.,\?\!\-]+$'
    return bool(re.match(pattern, text))

# ========== ОСНОВНЫЕ КОМАНДЫ ==========
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_question_mode[message.from_user.id] = False
    await message.answer(
        "👋 <b>Привет!</b>\n\n"
        "Я — ваш цифровой помощник Севастопольского городского онкологического диспансера имени А.А. Задорожного.\n\n"
        "Моя главная цель — сделать ваше взаимодействие с диспансером максимально простым и понятным.\n"
        "Я здесь, чтобы вы могли быстро сориентироваться в мире онкологической помощи, не теряясь в потоке информации.\n\n"
        "Что вас интересует?",
        parse_mode="HTML",
        reply_markup=main_menu_keyboard()
    )

@dp.message(Command("back"))
async def cmd_back(message: types.Message):
    user_question_mode[message.from_user.id] = False
    await message.answer(
        "🔙 Главное меню",
        reply_markup=main_menu_keyboard()
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📋 <b>Помощь</b>\n\n"
        "Используйте кнопки меню для навигации:\n"
        "• 🔍 Подготовка к исследованию - информация по анализам и процедурам\n"
        "• ❓ Часто-задаваемые вопросы - ответы на популярные вопросы\n"
        "• ✏️ Задать вопрос - связь с колл-центром",
        parse_mode="HTML"
    )

# ========== АДМИН-КОМАНДЫ ==========
@dp.message(Command("admin"))
async def admin_command(message: types.Message):
    await admin_panel(message)

@dp.message(Command("set_avatar"))
async def set_avatar_command(message: types.Message):
    await set_avatar(message)

@dp.message(Command("set_name"))
async def set_name_command(message: types.Message):
    await set_name(message)

@dp.message(Command("set_description"))
async def set_description_command(message: types.Message):
    await set_description(message)

@dp.message(Command("stats"))
async def stats_command(message: types.Message):
    await get_stats(message)

@dp.message(Command("broadcast"))
async def broadcast_command(message: types.Message):
    await broadcast(message)

# ==================================

# Обработчик главного меню
@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    user_question_mode[callback.from_user.id] = False
    await callback.message.edit_text(
        "👋 <b>Главное меню</b>\n\n"
        "Что вас интересует?",
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()

# Обработчик "Подготовка к исследованию"
@dp.callback_query(F.data == "research")
async def show_research(callback: types.CallbackQuery):
    user_question_mode[callback.from_user.id] = False
    await callback.message.edit_text(
        "🔍 Выберите вид диагностики:",
        reply_markup=research_keyboard()
    )
    await callback.answer()

# Обработчик "Назад к исследованиям"
@dp.callback_query(F.data == "back_to_research")
async def back_to_research(callback: types.CallbackQuery):
    user_question_mode[callback.from_user.id] = False
    await callback.message.edit_text(
        "🔍 Выберите вид диагностики:",
        reply_markup=research_keyboard()
    )
    await callback.answer()

# Обработчик "Задать вопрос" из главного меню
@dp.callback_query(F.data == "ask_question_main")
async def ask_question_main(callback: types.CallbackQuery):
    user_question_mode[callback.from_user.id] = True
    
    await callback.message.edit_text(
        "✏️ <b>Задайте ваш вопрос</b>\n\n"
        "Напишите ваш вопрос текстом.\n"
        "Разрешены только буквы, цифры и знаки препинания.\n\n"
        "❌ <b>Нельзя отправлять:</b>\n"
        "• Эмодзи и смайлики\n"
        "• Стикеры\n"
        "• Фото, видео, файлы\n"
        "• Ссылки\n\n"
        "Напишите ваш вопрос в этом чате 👇",
        parse_mode="HTML",
        reply_markup=cancel_question_keyboard()
    )
    await callback.answer()

# Обработчики выбора исследования
@dp.callback_query(F.data.startswith("research_"))
async def handle_research(callback: types.CallbackQuery):
    user_question_mode[callback.from_user.id] = False
    
    research_map = {
        "research_blood": ("🩸 Анализ крови", blood_analysis),
        "research_uzi": ("🔊 УЗИ брюшной полости", uzi),
        "research_fgds": ("🔬 ФГДС (гастроскопия)", fgds),
        "research_mrt": ("🖥️ МРТ/КТ с контрастом", mrt),
        "research_xray": ("📸 Рентген", xray),
        "research_ecg": ("🫀 ЭКГ/Холтер", ecg),
    }
    
    research_key = callback.data
    if research_key in research_map:
        name, handler = research_map[research_key]
        save_user_state(callback.from_user.id, research_key)
        
        class TempMessage:
            def __init__(self, answer_func):
                self.answer = answer_func
        
        async def answer_func(text, parse_mode=None, reply_markup=None):
            await callback.message.edit_text(
                text,
                parse_mode=parse_mode,
                reply_markup=back_to_research_keyboard()
            )
        
        temp_msg = TempMessage(answer_func)
        await handler(temp_msg)
    
    await callback.answer()

# Обработчик сообщений
@dp.message()
async def handle_messages(message: types.Message):
    if message.text and message.text.startswith('/'):
        return
    
    chat_id = message.from_user.id
    
    if user_question_mode.get(chat_id, False):
        if not message.text:
            await message.answer(
                "❌ Пожалуйста, отправляйте только текст.\n\n"
                "Нельзя отправлять фото, видео, файлы, стикеры или другие медиа.",
                reply_markup=cancel_question_keyboard()
            )
            return
        
        if not is_valid_text(message.text):
            await message.answer(
                "❌ Ваш вопрос содержит недопустимые символы.\n\n"
                "Разрешены только:\n"
                "• Буквы (русские и английские)\n"
                "• Цифры\n"
                "• Пробелы\n"
                "• Знаки: .,?!-\n\n"
                "Пожалуйста, напишите вопрос без эмодзи и специальных символов.",
                reply_markup=cancel_question_keyboard()
            )
            return
        
        if len(message.text) < 3:
            await message.answer(
                "❌ Вопрос слишком короткий.\n\n"
                "Пожалуйста, напишите более подробный вопрос (минимум 3 символа).",
                reply_markup=cancel_question_keyboard()
            )
            return
        
        if len(message.text) > 500:
            await message.answer(
                "❌ Вопрос слишком длинный.\n\n"
                "Пожалуйста, сократите вопрос (максимум 500 символов).",
                reply_markup=cancel_question_keyboard()
            )
            return
        
        user_question_mode[chat_id] = False
        
        await message.answer(
            "🤔 Я обучаюсь отвечать на вопросы из часто задаваемых и по подготовке.\n\n"
            "Пожалуйста, позвоните в колл-центр онкологического диспансера:\n"
            "📞 <b>+7 (8692) 24-02-46</b>\n\n"
            "Ваш вопрос не сохранён.\n\n"
            "🔙 Для возврата в меню нажмите кнопку ниже.",
            parse_mode="HTML",
            reply_markup=back_keyboard()
        )
        
    else:
        await message.answer(
            "❌ Пожалуйста, используйте только кнопки для навигации.\n\n"
            "Если хотите задать вопрос, нажмите кнопку «✏️ Задать вопрос» в главном меню.\n\n"
            "Вводить текст, отправлять стикеры, фото или файлы вне режима вопроса нельзя.",
            reply_markup=main_menu_keyboard()
        )

# Подключаем FAQ роутер
dp.include_router(faq_router)

async def main():
    print("🤖 Бот запущен!")
    print("✅ Команды: /start и /back")
    print("✅ Режим 'Задать вопрос' активен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())