from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.handlers.user.start import user_router
from app.models.models import Order, User
from app.states.user import OrderState
from app.keyboards.reply import main_menu

PRICES = {
    "📊 Taqdimot (Slayd)": 20000,
    "📄 Referat": 30000,
    "📑 Kurs ishi": 100000,
    "🎓 BMI": 150000,
    "🎓 Magistrlik dissertatsiyasi": 300000,
    "📝 Mustaqil ish": 20000,
    "📚 Dars ishlanma": 30000,
    "📋 Test yaratish": 15000,
    "🌐 Tarjimon": 5000,
    "📄 CV yaratish": 15000,
}

@user_router.message(F.text == "📋 Buyurtma berish")
async def start_order_flow(message: Message, state: FSMContext):
    await message.answer("Buyurtma qilmoqchi bo'lgan xizmat nomini menyulardan tanlang va bosing, "
                         "yoki qisqacha yozing.")
    await state.set_state(OrderState.choosing_service)
    
@user_router.message(OrderState.choosing_service)
async def service_chosen(message: Message, state: FSMContext):
    service = message.text
    price = PRICES.get(service, 20000)
    await state.update_data(service=service, price=price)
    
    await message.answer(f"Tanlangan xizmat: {service}\nNarxi (taxminiy): {price} so'm\n\nMavzuni kiriting:")
    await state.set_state(OrderState.entering_topic)

@user_router.message(OrderState.entering_topic)
async def topic_entered(message: Message, state: FSMContext):
    await state.update_data(topic=message.text)
    await message.answer("Qanday qo'shimcha talablaringiz bor? (Yoki 'yoq' deb yozing)")
    await state.set_state(OrderState.entering_requirements)
    
@user_router.message(OrderState.entering_requirements)
async def requirements_entered(message: Message, state: FSMContext):
    await state.update_data(requirements=message.text)
    await message.answer("Bunga doir fayl bo'lsa yuklang (agar bo'lmasa qisqacha 'yoq' deb yozing):")
    await state.set_state(OrderState.uploading_file)

@user_router.message(OrderState.uploading_file)
async def file_uploaded(message: Message, state: FSMContext, db_user: User, session):
    data = await state.get_data()
    file_id = ""
    if getattr(message, "document", None):
        file_id = message.document.file_id
    elif getattr(message, "photo", None):
        file_id = message.photo[-1].file_id
        
    price = data['price']
    
    if db_user.balance < price:
        await message.answer(f"❌ Balansingizda mablag‘ yetarli emas.\nKerakli summa: {price} so'm.\nIltimos, balansingizni to'ldiring.", reply_markup=main_menu())
        await state.clear()
        return
        
    db_user.balance -= price
    
    desc = f"Mavzu: {data['topic']}\nTalablar: {data['requirements']}"
    order = Order(user_id=db_user.id, service=data['service'], description=desc, file_url=file_id, price=price)
    session.add(order)
    await session.commit()
    
    await message.answer(f"✅ Buyurtma qabul qilindi. Balansingizdan {price} so'm yechildi.", reply_markup=main_menu())
    await state.clear()
