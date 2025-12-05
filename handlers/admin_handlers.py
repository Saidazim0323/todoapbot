from aiogram import Router
from aiogram.types import Message
from config import SUPER_ADMIN_ID

router = Router()

def register_admin_handlers(dp):
    dp.include_router(router)

@router.message()
async def admin_panel(msg: Message):
    if msg.from_user.id != SUPER_ADMIN_ID:
        return
    await msg.answer("Admin panelga xush kelibsiz!")
