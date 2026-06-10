from aiogram import F
from aiogram.types import Message
from app.keyboards.reply import teacher_menu
from app.handlers.user.start import user_router

@user_router.message(F.text == "👨🏫 O‘qituvchilar uchun")
async def teacher_section(message: Message):
    await message.answer("O‘qituvchilar uchun xizmatlar:", reply_markup=teacher_menu())
