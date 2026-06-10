from aiogram import F
from aiogram.types import Message
from sqlalchemy.future import select
from sqlalchemy import func
from app.handlers.user.start import user_router
from app.models.models import Order, User
from app.keyboards.inline import tariffs_keyboard

@user_router.message(F.text == "👤 Profil")
async def view_profile(message: Message, db_user: User, session):
    order_count_result = await session.execute(select(func.count(Order.id)).where(Order.user_id == db_user.id))
    order_count = order_count_result.scalar()
    
    date_str = db_user.created_at.strftime("%Y-%m-%d %H:%M")
    
    text = f"👤 Ism: {db_user.fullname}\n" \
           f"🆔 Telegram ID: {db_user.telegram_id}\n" \
           f"📛 Username: @{db_user.username}\n" \
           f"💰 Balans: {db_user.balance} so'm\n" \
           f"⭐ Tarif: {db_user.tariff.value} (so'rovlar: {db_user.requests_left})\n" \
           f"📦 Buyurtmalar soni: {order_count}\n" \
           f"📅 Ro‘yxatdan o‘tgan sana: {date_str}"
           
    await message.answer(text, reply_markup=tariffs_keyboard())

@user_router.message(F.text == "⭐ Buyurtmalarim")
async def view_my_orders(message: Message, db_user: User, session):
    orders_rs = await session.execute(select(Order).where(Order.user_id == db_user.id).limit(10).order_by(Order.id.desc()))
    orders = orders_rs.scalars().all()
    
    if not orders:
        await message.answer("Sizda hali buyurtmalar yo'q.")
        return
        
    text = "Sizning so'nggi buyurtmalaringiz:\n\n"
    for idx, order in enumerate(orders, 1):
        text += f"{idx}. {order.service} - {order.price} so'm\nHolati: {order.status.value}\nSana: {order.created_at.strftime('%Y-%m-%d %H:%M')}\n\n"
    
    await message.answer(text)

@user_router.message(F.text == "📞 Operator")
async def call_operator(message: Message):
    await message.answer("📞 Operator bilan bog'lanish:\nTelegram: @Ta'lim_operatori\nTelefon: +998 90 123 45 67")
    
@user_router.message(F.text == "ℹ️ Bot haqida")
async def about_bot(message: Message):
    await message.answer("Taqdimot va professional ta'lim xizmatlari boti.\nSiz bu yerda o'quv ishlaringizni buyurtma qilishingiz mumkin.")

from aiogram.types import CallbackQuery
from app.models.models import TariffEnum

@user_router.callback_query(F.data.startswith("buy_"))
async def buy_tariff(callback: CallbackQuery, db_user: User, session):
    tariff_type = callback.data.split("_")[1] # basic, premium, vip
    
    prices = {
        "basic": 29000,
        "premium": 79000,
        "vip": 149000
    }
    
    requests = {
        "basic": 10,
        "premium": 100,
        "vip": 999999
    }
    
    enums = {
        "basic": TariffEnum.BASIC,
        "premium": TariffEnum.PREMIUM,
        "vip": TariffEnum.VIP
    }
    
    price = prices.get(tariff_type)
    
    if db_user.balance < price:
        await callback.answer(f"❌ Balansingizda mablag‘ yetarli emas.\nKerakli summa: {price} so'm.", show_alert=True)
        return
        
    db_user.balance -= price
    db_user.tariff = enums[tariff_type]
    db_user.requests_left = requests[tariff_type]
    
    await session.commit()
    
    await callback.message.edit_reply_markup()
    await callback.message.reply(f"✅ Tabriklaymiz! Siz {enums[tariff_type].value} tarifini sotib oldingiz.")

