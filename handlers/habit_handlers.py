from aiogram import Router, types
from database import connect_db

habit_router = Router()

@habit_router.message(commands=["habit"])
async def add_habit(msg: types.Message):
    habit = msg.text.replace("/habit", "").strip()

    conn = await connect_db()
    await conn.execute("INSERT INTO habits (user_id, habit) VALUES ($1,$2)", msg.from_user.id, habit)
    await conn.close()

    await msg.answer("💪 Odatingiz qo‘shildi!")
