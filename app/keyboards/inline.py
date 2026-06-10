from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def payment_confirm(payment_id: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"pay_approve_{payment_id}"),
                InlineKeyboardButton(text="❌ Rad etish", callback_data=f"pay_reject_{payment_id}")
            ]
        ]
    )
    return markup

def tariffs_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🥉 BASIC - 29 000 so‘m", callback_data="buy_basic")],
            [InlineKeyboardButton(text="🥈 PREMIUM - 79 000 so‘m", callback_data="buy_premium")],
            [InlineKeyboardButton(text="🥇 VIP - 149 000 so‘m", callback_data="buy_vip")]
        ]
    )
    return markup
