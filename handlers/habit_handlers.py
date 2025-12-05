from aiogram import Router
from aiogram.types import Message

router = Router()

def register_habit_handlers(dp):
    dp.include_router(router)

@router.message()
async def habits(msg: Message):
    if msg.text == "/habit":
        await msg.answer("🔹 Bu yerda odatlar bo'ladi.")
