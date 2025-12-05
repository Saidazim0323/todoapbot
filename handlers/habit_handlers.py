from aiogram import Router, types, F
from database import create_pool

habit_router = Router()

def register_habit_handlers(dp):
    dp.include_router(habit_router)

@habit_router.message(F.text.startswith("/habit"))
async def add_habit(msg: types.Message):
    habit = msg.text.replace("/habit", "").strip()

    if not habit:
        return await msg.answer("❌ Odat kiriting. Masalan: /habit Meditatsiya")

    pool = await create_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            "INSERT INTO habits (user_id, habit) VALUES ($1, $2)",
            msg.from_user.id, habit
        )

    await msg.answer(f"💪 Odat qo‘shildi: {habit}")
