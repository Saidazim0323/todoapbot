from aiogram import BaseMiddleware
from config import SUPER_ADMIN_ID

class AdminCheck(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if event.from_user.id != SUPER_ADMIN_ID:
            return
        return await handler(event, data)
