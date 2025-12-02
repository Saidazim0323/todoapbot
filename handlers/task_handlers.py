from aiogram import Router, types
from database import connect_db

task_router = Router()

@task_router.message(commands=["task"])
async def add_task(msg: types.Message):
    title = msg.text.replace("/task", "").strip()
    if not title:
        return await msg.answer("Vazifa yozing: /task Kitob o‘qish")

    conn = await connect_db()
    await conn.execute("INSERT INTO tasks (user_id, title) VALUES ($1,$2)", msg.from_user.id, title)
    await conn.close()

    await msg.answer("✅ Vazifa qo‘shildi.")
