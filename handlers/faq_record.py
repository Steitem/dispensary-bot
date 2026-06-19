from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def faq_record(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔗 Перейти на Госуслуги", url="https://www.gosuslugi.ru")],
        [InlineKeyboardButton(text="📱 Скачать приложение Госуслуги", url="https://www.gosuslugi.ru/application")],
        [InlineKeyboardButton(text="🔙 Назад в FAQ", callback_data="faq_home")]
    ])

    await message.answer(
        "📅 <b>Как записаться на приём к врачу?</b>\n\n"
        "Запись на приём к врачу-онкологу в наш диспансер осуществляется <b>строго по направлению</b> от врача из поликлиники по месту вашего жительства.\n\n"
        "• <b>Основной способ</b> — по единому короткому номеру <b>«122»</b>. Звонок бесплатный с любых телефонов, служба работает круглосуточно.\n"
        "• <b>Дополнительные телефоны регистратуры:</b>\n"
        "  📞 +7 (978) 254-50-08\n"
        "  📞 +7 (8692) 41-77-15\n"
        "  📞 +7 (8692) 24-02-04\n"
        "• Самостоятельная запись через портал <b>«Госуслуги»</b> ограничена, так как мы оказываем специализированную помощь.\n"
        "• Если у вас <b>нет направления</b>, вы можете получить платную консультацию. Подробности уточняйте в регистратуре по телефону <b>+7 (8692) 41-77-15</b>.",
        reply_markup=keyboard,
        parse_mode="HTML"
    )