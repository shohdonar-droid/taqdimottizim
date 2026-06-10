import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_IDS = [int(admin_id) for admin_id in os.getenv("ADMIN_IDS", "").split(",") if admin_id]
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///bot.db") # default to local sqlite
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://")
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

UZCARD_NUMBER = os.getenv("UZCARD_NUMBER", "8600 1234 5678 9012")
HUMO_NUMBER = os.getenv("HUMO_NUMBER", "9860 1234 5678 9012")
CARD_HOLDER = os.getenv("CARD_HOLDER", "ELYORBEK ORTIQOV")
