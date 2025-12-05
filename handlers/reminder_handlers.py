from aiogram import Router, types
from aiogram.filters import Command
from database import create_pool

reminder_router = Router()

def register_reminder_handlers(dp):
    dp.include_router(reminder_router)

@reminder_router.message(Command("time"))
async def set_time(msg: types.Message):
    try:
        hour = int(msg.text.split()[1])
    except:
        return await msg.answer("To‘g‘ri format: /time 9")

    if hour < 0 or hour > 23:
        return await msg.answer("0-23 orasida soat kiriting.")

    pool = await create_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            "UPDATE users SET reminder_hour=$1 WHERE user_id=$2",
            hour, msg.from_user.id
        )

    await msg.answer(f"🔔 Eslatma vaqti: {hour}:00")
