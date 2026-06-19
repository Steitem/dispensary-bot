from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def faq_home(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Как записаться на приём к врачу?", callback_data="faq_record")],
        [InlineKeyboardButton(text="📊 Как получить результаты анализов?", callback_data="faq_results")],
        [InlineKeyboardButton(text="⏰ Можно ли прийти без записи (живая очередь)?", callback_data="faq_queue")],
        [InlineKeyboardButton(text="🔄 Как отменить или перенести запись?", callback_data="faq_cancel")],
        [InlineKeyboardButton(text="🆔 Что делать, если я потерял полис/сменил фамилию?", callback_data="faq_policy")],
        [InlineKeyboardButton(text="📋 Справка для работы (форма 086/у)?", callback_data="faq_medical_certificate")],
        [InlineKeyboardButton(text="🩺 Когда проводится диспансеризация и кто может её пройти?", callback_data="faq_dispanserization")],
        [InlineKeyboardButton(text="🏠 Можно ли вызвать врача на дом и как это сделать?", callback_data="faq_home_call")],
        [InlineKeyboardButton(text="📸 Нужно ли проходить флюорографию ежегодно и где взять направление?", callback_data="faq_fluorography")],
        [InlineKeyboardButton(text="📅 Работает ли диспансер в выходные и праздничные дни?", callback_data="faq_weekend")],
        [InlineKeyboardButton(text="💊 Как получить рецепт на льготные лекарства (бесплатно)?", callback_data="faq_medicines")],
        [InlineKeyboardButton(text="📄 Как закрыть или продлить больничный лист?", callback_data="faq_sick_leave")],
        [InlineKeyboardButton(text="🔙 Назад в главное меню", callback_data="back_to_main")]
    ])

    await message.answer(
        "<b>❓ Часто-задаваемые вопросы</b>\n\n"
        "Выберите вопрос, чтобы получить подробный ответ:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )