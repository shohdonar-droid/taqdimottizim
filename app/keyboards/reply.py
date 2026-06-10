from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Talabalar uchun"), KeyboardButton(text="👨🏫 O‘qituvchilar uchun")],
            [KeyboardButton(text="🤖 AI Xizmatlar"), KeyboardButton(text="📋 Buyurtma berish")],
            [KeyboardButton(text="💰 Balans"), KeyboardButton(text="💳 Balansni to‘ldirish")],
            [KeyboardButton(text="⭐ Buyurtmalarim"), KeyboardButton(text="👤 Profil")],
            [KeyboardButton(text="📞 Operator"), KeyboardButton(text="ℹ️ Bot haqida")]
        ],
        resize_keyboard=True
    )
    return markup
    
def student_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Taqdimot (Slayd)"), KeyboardButton(text="📄 Referat")],
            [KeyboardButton(text="📑 Kurs ishi"), KeyboardButton(text="🎓 BMI")],
            [KeyboardButton(text="🎓 Magistrlik dissertatsiyasi"), KeyboardButton(text="📝 Mustaqil ish")],
            [KeyboardButton(text="📚 Amaliyot hisobotlari"), KeyboardButton(text="📖 Annotatsiya")],
            [KeyboardButton(text="📋 Taqriz"), KeyboardButton(text="📄 Adabiyotlar ro'yxati")],
            [KeyboardButton(text="🏠 Bosh sahifa")],
        ],
        resize_keyboard=True
    )
    return markup

def teacher_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Dars ishlanma"), KeyboardButton(text="📅 Taqvim-mavzu reja")],
            [KeyboardButton(text="📋 Test yaratish"), KeyboardButton(text="📄 Ilmiy maqola formatlash")],
            [KeyboardButton(text="📚 Elektron qo'llanma"), KeyboardButton(text="🔍 Antiplagiat tekshiruvi")],
            [KeyboardButton(text="🏠 Bosh sahifa")],
        ],
        resize_keyboard=True
    )
    return markup

def ai_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⭐ Slayd yaratish"), KeyboardButton(text="⭐ Kurs ishi bo‘yicha yordam")],
            [KeyboardButton(text="⭐ Tezis yaratish"), KeyboardButton(text="⭐ Maqola yaratish")],
            [KeyboardButton(text="⭐ Dars ishlanma yaratish"), KeyboardButton(text="⭐ Test yaratish")],
            [KeyboardButton(text="⭐ Tarjimon"), KeyboardButton(text="⭐ CV yaratish")],
            [KeyboardButton(text="⭐ Motivatsion xat"), KeyboardButton(text="⭐ Rezyume yaratish")],
            [KeyboardButton(text="⭐ AI Chat"), KeyboardButton(text="🏠 Bosh sahifa")],
        ],
        resize_keyboard=True
    )
    return markup
    
def admin_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Statistika"), KeyboardButton(text="👥 Foydalanuvchilar soni")],
            [KeyboardButton(text="💰 Jami daromad"), KeyboardButton(text="📦 Buyurtmalar soni")],
            [KeyboardButton(text="💳 To‘lovlar"), KeyboardButton(text="📢 Reklama yuborish")],
            [KeyboardButton(text="👤 Foydalanuvchini bloklash"), KeyboardButton(text="👤 Foydalanuvchini ochish")],
            [KeyboardButton(text="💰 Balans qo‘shish"), KeyboardButton(text="💰 Balans ayirish")],
            [KeyboardButton(text="📦 Buyurtmalarni ko‘rish"), KeyboardButton(text="📋 Xizmatlar narxini o‘zgartirish")],
            [KeyboardButton(text="🏠 Bosh sahifa")]
        ],
        resize_keyboard=True
    )
    return markup

def cancel_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="❌ Bekor qilish")]],
        resize_keyboard=True
    )
