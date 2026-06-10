from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.keyboards.reply import main_menu

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message, db_user):
    text = f"Assalomu alaykum, {message.from_user.full_name}!\n\n" \
           f"Taqdimot va ta'lim xizmatlari botiga xush kelibsiz.\n" \
           f"Quyidagi menyudan kerakli bo'limni tanlang:"
    await message.answer(text, reply_markup=main_menu())

@user_router.message(F.text == "🏠 Bosh sahifa")
async def process_home(message: Message):
    await message.answer("Bosh sahifaga qaytdingiz.", reply_markup=main_menu())
