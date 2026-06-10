from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.future import select
from app.database.database import async_session
from app.models.models import User

class DatabaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        async with async_session() as session:
            data['session'] = session
            # Retrieve or create user if it's a message or callback
            event_user = getattr(event, "from_user", None)
            if event_user:
                result = await session.execute(select(User).where(User.telegram_id == event_user.id))
                user = result.scalar_one_or_none()
                if not user:
                    user = User(
                        telegram_id=event_user.id,
                        fullname=event_user.full_name,
                        username=event_user.username,
                    )
                    session.add(user)
                    await session.commit()
                data['db_user'] = user
                
            return await handler(event, data)
