from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.handlers.user.start import user_router
from app.config.config import UZCARD_NUMBER, HUMO_NUMBER, CARD_HOLDER, ADMIN_IDS
from app.states.user import PaymentState
from app.models.models import Payment, User
from app.keyboards.inline import payment_confirm
from app.keyboards.reply import main_menu

@user_router.message(F.text == "💰 Balans")
async def show_balance(message: Message, db_user):
    text = f"💰 Joriy balansingiz: {db_user.balance} so'm\n⭐ Tarifingiz: {db_user.tariff.value}\n🤖 Qolgan AI so'rovlar: {db_user.requests_left}"
    await message.answer(text)

@user_router.message(F.text == "💳 Balansni to‘ldirish")
async def fill_balance(message: Message, state: FSMContext):
    text = f"💳 Uzcard\n`{UZCARD_NUMBER}`\n\n" \
           f"💳 Humo\n`{HUMO_NUMBER}`\n\n" \
           f"👤 Karta egasi: {CARD_HOLDER}\n\n" \
           f"Pul o'tkazganingizdan so‘ng:\n" \
           f"📷 Chek rasmini yuboring"
    await message.answer(text, parse_mode="Markdown")
    await state.set_state(PaymentState.uploading_receipt)

@user_router.message(PaymentState.uploading_receipt, F.photo)
async def receipt_uploaded(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(receipt_photo=photo_id)
    await message.answer("💰 To‘langan summani faqat raqamlarda kiriting (masalan: 50000):")
    await state.set_state(PaymentState.entering_amount)

@user_router.message(PaymentState.entering_amount)
async def amount_entered(message: Message, state: FSMContext, db_user: User, session):
    if not message.text.isdigit():
        await message.answer("Iltimos, faqat raqam kiriting.")
        return
        
    amount = int(message.text)
    data = await state.get_data()
    photo_id = data.get("receipt_photo")
    
    payment = Payment(user_id=db_user.id, amount=amount, receipt_photo=photo_id)
    session.add(payment)
    await session.commit()
    
    await message.answer("✅ To‘lov ma'lumotlari adminga yuborildi. Tasdiqlanishini kuting.", reply_markup=main_menu())
    await state.clear()
    
    admin_text = f"🧾 Yangi to‘lov so‘rovi\n\n" \
                 f"👤 Ism: {db_user.fullname}\n" \
                 f"🆔 Telegram ID: {db_user.telegram_id}\n" \
                 f"📛 Username: @{db_user.username}\n" \
                 f"💰 Summa: {amount} so'm"
    
    for admin in ADMIN_IDS:
        try:
            await message.bot.send_photo(admin, photo=photo_id, caption=admin_text, reply_markup=payment_confirm(payment.id))
        except Exception:
            pass
