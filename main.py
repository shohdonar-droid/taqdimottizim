from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from app.config.config import BOT_TOKEN
from app.database.database import init_db
from app.utils.logging import setup_logging
from app.middlewares.db import DatabaseMiddleware
import logging

async def main():
    setup_logging()
    
    if not BOT_TOKEN:
        logging.error("BOT_TOKEN is missing!")
        return

    await init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    
    # Register global middleware
    dp.update.middleware(DatabaseMiddleware())
    
    # Imports inside main to avoid circular dependencies
    from app.handlers.user.start import user_router
    from app.handlers.admin.panel import admin_router
    
    dp.include_router(user_router)
    dp.include_router(admin_router)
    
    logging.info("Bot is starting up...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
