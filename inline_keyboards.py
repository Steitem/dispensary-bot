from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 Подготовка к исследованию", callback_data="research")],
        [InlineKeyboardButton(text="❓ Часто-задаваемые вопросы", callback_data="faq_home")],
        [InlineKeyboardButton(text="✏️ Задать вопрос", callback_data="ask_question_main")]  # ← НОВАЯ КНОПКА
    ])

def research_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🩸 Анализ крови", callback_data="research_blood")],
        [InlineKeyboardButton(text="🔊 УЗИ брюшной полости", callback_data="research_uzi")],
        [InlineKeyboardButton(text="🔬 ФГДС (гастроскопия)", callback_data="research_fgds")],
        [InlineKeyboardButton(text="🖥️ МРТ/КТ с контрастом", callback_data="research_mrt")],
        [InlineKeyboardButton(text="📸 Рентген", callback_data="research_xray")],
        [InlineKeyboardButton(text="🫀 ЭКГ/Холтер", callback_data="research_ecg")],
        [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_main")]
    ])

def back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ])

def back_to_research_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться к исследованиям", callback_data="back_to_research")]
    ])

def research_done_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться к списку исследований", callback_data="back_to_research")]
    ])

def cancel_question_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Отменить и вернуться в меню", callback_data="back_to_main")]
    ])