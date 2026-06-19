from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🩸 Анализ крови (общий/биохимия)")],
        [KeyboardButton(text="🔊 УЗИ брюшной полости")],
        [KeyboardButton(text="🔬 ФГДС (гастроскопия)")],
        [KeyboardButton(text="🖥️ МРТ/КТ с контрастом")],
        [KeyboardButton(text="📸 Рентген")],
        [KeyboardButton(text="🫀 ЭКГ/Холтер")],
        [KeyboardButton(text="❓ Часто-задаваемые вопросы")],
        [KeyboardButton(text="📋 Помощь")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите исследование..."
)