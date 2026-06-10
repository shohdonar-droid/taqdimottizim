from aiogram import F
from aiogram.types import CallbackQuery
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.handlers.admin.panel import admin_router, is_admin
from app.models.models import Payment, PaymentStatus
from app.database.database import async_session

@admin_router.callback_query(F.data.startswith("pay_approve_"))
async def approve_payment(callback: CallbackQuery):
    if not is_admin(callback.from_user.id):
        return
        
    payment_id = int(callback.data.split("_")[-1])
    async with async_session() as session:
        result = await session.execute(select(Payment).options(selectinload(Payment.user)).where(Payment.id == payment_id))
        payment = result.scalar_one_or_none()
        
        if not payment or payment.status != PaymentStatus.PENDING:
            await callback.answer("To'lov allaqachon ko'rib chiqilgan yoki topilmadi.", show_alert=True)
            return
            
        payment.status = PaymentStatus.APPROVED
        payment.user.balance += payment.amount
        await session.commit()
        
        await callback.message.edit_reply_markup()
        await callback.message.reply("✅ To'lov tasdiqlandi!")
        
        try:
            await callback.bot.send_message(
                payment.user.telegram_id, 
                f"✅ To‘lov muvaffaqiyatli tasdiqlandi\n💰 Balansingizga {payment.amount} so‘m qo‘shildi\n\nJoriy balans: {payment.user.balance} so‘m"
            )
        except:
            pass

@admin_router.callback_query(F.data.startswith("pay_reject_"))
async def reject_payment(callback: CallbackQuery):
    if not is_admin(callback.from_user.id):
        return
        
    payment_id = int(callback.data.split("_")[-1])
    async with async_session() as session:
        result = await session.execute(select(Payment).options(selectinload(Payment.user)).where(Payment.id == payment_id))
        payment = result.scalar_one_or_none()
        
        if not payment or payment.status != PaymentStatus.PENDING:
            await callback.answer("To'lov allaqachon ko'rib chiqilgan yoki topilmadi.", show_alert=True)
            return
            
        payment.status = PaymentStatus.REJECTED
        await session.commit()
        
        await callback.message.edit_reply_markup()
        await callback.message.reply("❌ To'lov rad etildi!")
        
        try:
            await callback.bot.send_message(
                payment.user.telegram_id, 
                f"❌ To‘lov rad etildi\nIltimos chekni qayta yuboring yoki operator bilan bog‘laning."
            )
        except:
            pass
