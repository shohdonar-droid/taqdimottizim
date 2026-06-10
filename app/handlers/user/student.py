from aiogram import F
from aiogram.types import Message
from app.keyboards.reply import student_menu
from app.handlers.user.start import user_router

@user_router.message(F.text == "📚 Talabalar uchun")
async def student_section(message: Message):
    await message.answer("Talabalar uchun xizmatlar:", reply_markup=student_menu())
