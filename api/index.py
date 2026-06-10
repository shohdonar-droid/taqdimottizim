import os
import sys

# Project root-ni modullarga qo'shamiz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

app = FastAPI()

try:
    from app.config.config import BOT_TOKEN
    from app.database.database import init_db
    from app.middlewares.db import DatabaseMiddleware
    
    from app.handlers.user import user_router
    from app.handlers.admin import admin_router
    
    bot = Bot(token=BOT_TOKEN) if BOT_TOKEN else None
    dp = Dispatcher(storage=MemoryStorage())
    
    dp.update.middleware(DatabaseMiddleware())
    dp.include_router(user_router)
    dp.include_router(admin_router)
except Exception as e:
    print(f"Failed to initialize configs: {e}")
    bot = None
    dp = None

@app.on_event("startup")
async def on_startup():
    if bot:
        try:
            await init_db()
        except Exception as e:
            print(f"Error initializing database: {e}")

@app.post("/api/webhook")
async def webhook_handler(request: Request):
    if not bot:
        return {"status": "error", "message": "BOT_TOKEN not set"}
        
    try:
        update_data = await request.json()
        update = types.Update(**update_data)
        await dp.feed_update(bot=bot, update=update)
        return {"status": "ok"}
    except Exception as e:
        print(f"Webhook error: {e}")
        return {"status": "error", "message": str(e)}
        
@app.get("/api/set_webhook")
async def set_webhook(url: str):
    if not bot:
        return {"status": "error", "message": "BOT_TOKEN not set"}
        
    webhook_url = f"{url.rstrip('/')}/api/webhook"
    try:
        await bot.set_webhook(webhook_url)
        return {"status": "ok", "message": f"Webhook configured: {webhook_url}"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to set webhook: {e}"}

@app.get("/")
async def index():
    return {"status": "Aiogram 3 Bot is active on Vercel!"}
