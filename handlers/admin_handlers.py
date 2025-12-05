# handlers/admin_handlers.py
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from config import SUPER_ADMIN_ID

admin_router = Router()

def register_admin_handlers(dp):
    dp.include_router(admin_router)
@admin_router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Assalomu alaykum! Botdan foydalanishni boshlashingiz mumkin 😊")

# Faqat /admin komandasi kelganda ishlaydi
@admin_router.message(Command("admin"))
async def admin_panel(msg: Message):
    if msg.from_user.id != SUPER_ADMIN_ID:
        return await msg.answer("❌ Siz admin emassiz!")

    await msg.answer("🔐 Admin paneliga xush kelibsiz!")
