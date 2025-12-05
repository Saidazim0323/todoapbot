# handlers/admin_handlers.py
from aiogram import Router
from aiogram.types import Message
from config import SUPER_ADMIN_ID

admin_router = Router()

def register_admin_handlers(dp):
    dp.include_router(admin_router)


@admin_router.message()
async def admin_panel(msg: Message):
    if msg.from_user.id != SUPER_ADMIN_ID:
        return
    
    await msg.answer("🔐 Admin panelga xush kelibsiz!")
