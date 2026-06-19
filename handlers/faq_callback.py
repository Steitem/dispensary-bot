from aiogram import types
from aiogram import Router, F

router = Router()

# Импортируем все FAQ функции
from .faq_record import faq_record
from .faq_results import faq_results
from .faq_queue import faq_queue
from .faq_cancel import faq_cancel
from .faq_policy import faq_policy
from .faq_medical_certificate import faq_medical_certificate
from .faq_dispanserization import faq_dispanserization
from .faq_home_call import faq_home_call
from .faq_fluorography import faq_fluorography
from .faq_weekend import faq_weekend
from .faq_medicines import faq_medicines
from .faq_sick_leave import faq_sick_leave

@router.callback_query(F.data.startswith("faq_"))
async def handle_faq_callback(callback: types.CallbackQuery):
    if callback.data == "faq_record":
        await faq_record(callback.message)
    elif callback.data == "faq_results":
        await faq_results(callback.message)
    elif callback.data == "faq_queue":
        await faq_queue(callback.message)
    elif callback.data == "faq_cancel":
        await faq_cancel(callback.message)
    elif callback.data == "faq_policy":
        await faq_policy(callback.message)
    elif callback.data == "faq_medical_certificate":
        await faq_medical_certificate(callback.message)
    elif callback.data == "faq_dispanserization":
        await faq_dispanserization(callback.message)
    elif callback.data == "faq_home_call":
        await faq_home_call(callback.message)
    elif callback.data == "faq_fluorography":
        await faq_fluorography(callback.message)
    elif callback.data == "faq_weekend":
        await faq_weekend(callback.message)
    elif callback.data == "faq_medicines":
        await faq_medicines(callback.message)
    elif callback.data == "faq_sick_leave":
        await faq_sick_leave(callback.message)
    elif callback.data == "faq_home":
        from .faq_home import faq_home
        await faq_home(callback.message)
    
    await callback.answer()

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    from inline_keyboards import main_menu_keyboard
    
    await callback.message.edit_text(
        "👋 <b>Главное меню</b>\n\n"
        "Что вас интересует?",
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()