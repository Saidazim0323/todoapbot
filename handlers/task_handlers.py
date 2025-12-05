from aiogram import Router, types, F
from database import create_pool

task_router = Router()

@task_router.message(F.text.startswith("/task"))
async def add_task(msg: types.Message):
    title = msg.text.replace("/task", "").strip()

    if not title:
        return await msg.answer("Vazifa yozing: /task Kitob o‘qish")

    pool = await create_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            "INSERT INTO tasks (user_id, title) VALUES ($1, $2)",
            msg.from_user.id, title
        )

    await msg.answer("✅ Vazifa qo‘shildi.")


# 🔥 MUHIM: Bu funksiyani qo‘shmasang import error bo‘ladi!
def register_task_handlers(dp):
    dp.include_router(task_router)
