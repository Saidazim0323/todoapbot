from aiogram import Router, types
from config import ADMIN_ID

admin_router = Router()

@admin_router.message(lambda m: m.from_user.id == ADMIN_ID)
async def admin_panel(msg: types.Message):
    await msg.answer("🔐 Admin paneliga xush kelibsiz!")
