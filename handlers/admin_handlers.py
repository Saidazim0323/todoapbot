from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from config import SUPER_ADMIN_ID

admin_router = Router()

def register_admin_handlers(dp):
    dp.include_router(admin_router)

@admin_router.message(Command("admin"))
async def admin_panel(msg: Message):
    if msg.from_user.id != SUPER_ADMIN_ID:
        return await msg.answer("❌ Siz adminsiz!")

    await msg.answer("🔐 Admin panelga xush kelibsiz!")
