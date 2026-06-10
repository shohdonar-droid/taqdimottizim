from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy.future import select
from sqlalchemy import func
from app.config.config import ADMIN_IDS
from app.models.models import User, Order, Payment
from app.keyboards.reply import admin_menu
from aiogram.filters import Command

admin_router = Router()

def is_admin(user_id: int):
    return user_id in ADMIN_IDS

@admin_router.message(Command("admin"))
async def admin_panel_start(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer("Admin paneliga xush kelibsiz!", reply_markup=admin_menu())

@admin_router.message(F.text == "📊 Statistika")
async def view_stats(message: Message, session):
    if not is_admin(message.from_user.id):
        return
        
    user_count = await session.execute(select(func.count(User.id)))
    users = user_count.scalar()
    
    order_count = await session.execute(select(func.count(Order.id)))
    orders = order_count.scalar()
    
    revenue_sum = await session.execute(select(func.sum(Order.price)))
    revenue = revenue_sum.scalar() or 0
    
    text = f"📊 Statistika:\n\n" \
           f"👥 Foydalanuvchilar soni: {users}\n" \
           f"📦 Buyurtmalar soni: {orders}\n" \
           f"💰 Jami daromad (xizmatlardan): {revenue} so'm"
           
    await message.answer(text)
    
# Admin features like broadcasting, ban, add balance could be added here similar to standard FSM flows
