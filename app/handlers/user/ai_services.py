from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.keyboards.reply import ai_menu, cancel_menu, main_menu
from app.handlers.user.start import user_router
from app.services.gemini import gemini_service
from app.states.user import AIChatState
from app.models.models import User

AI_SERVICES = [
    "⭐ Slayd yaratish", "⭐ Kurs ishi bo‘yicha yordam", 
    "⭐ Tezis yaratish", "⭐ Maqola yaratish",
    "⭐ Dars ishlanma yaratish", "⭐ Test yaratish",
    "⭐ Tarjimon", "⭐ CV yaratish", 
    "⭐ Motivatsion xat", "⭐ Rezyume yaratish"
]

@user_router.message(F.text == "🤖 AI Xizmatlar")
async def ai_section(message: Message):
    await message.answer("AI xizmatlarini tanlang:", reply_markup=ai_menu())

@user_router.message(F.text == "⭐ AI Chat")
async def ai_chat_start(message: Message, state: FSMContext, db_user: User):
    if db_user.requests_left <= 0:
        await message.answer("Sizning tarifingiz bo'yicha so'rovlar tugadi. Iltimos tarifni yangilang.")
        return
    await state.set_state(AIChatState.chatting)
    await message.answer("AI Chatga xush kelibsiz! Savolingizni yuboring. Chiqish uchun '❌ Bekor qilish' ni bosing.", reply_markup=cancel_menu())

@user_router.message(AIChatState.chatting, F.text == "❌ Bekor qilish")
async def ai_chat_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("AI Chat yakunlandi.", reply_markup=ai_menu())

@user_router.message(AIChatState.chatting)
async def ai_chat_process(message: Message, state: FSMContext, db_user: User, session):
    if db_user.requests_left <= 0:
        await message.answer("Sizning tarifingiz bo'yicha so'rovlar tugadi.", reply_markup=ai_menu())
        await state.clear()
        return

    db_user.requests_left -= 1
    await session.commit()

    wait_msg = await message.answer("✍️ Yozmoqda...")
    response_text = gemini_service.generate_response(message.text, "Sen aqlli ta'lim yordamchisan.")
    await wait_msg.delete()
    await message.answer(response_text)

@user_router.message(F.text.in_(AI_SERVICES))
async def specific_ai_service(message: Message, db_user: User, session):
    if db_user.requests_left <= 0:
        await message.answer("Sizning tarifingiz bo'yicha so'rovlar tugadi. Iltimos tarifni yangilang.")
        return

    db_user.requests_left -= 1
    await session.commit()

    wait_msg = await message.answer("AI xizmati ishlayapti, kuting...")
    
    prompt = f"Menga shu mavzuda yordam bering: {message.text}. Iltimos, mutaxassisdek batafsil ma'lumot tayyorlang."
    response = gemini_service.generate_response(prompt, f"Foydalanuvchi quyidagi AI xizmatni tanladi: {message.text}.")
    
    await wait_msg.delete()
    await message.answer(response)
