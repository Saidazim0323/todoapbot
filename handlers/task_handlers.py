# handlers/task_handlers.py
import logging
from aiogram import Router, types
from aiogram.filters import Command
from database import create_pool

logger = logging.getLogger(__name__)
task_router = Router()

def register_task_handlers(dp):
    dp.include_router(task_router)

@task_router.message(Command("task"))
async def add_task(msg: types.Message):
    logger.info("add_task called: user=%s text=%s", getattr(msg.from_user, "id", None), msg.text)
    text = msg.text or ""
    title = text.replace("/task", "", 1).strip()

    if not title:
        return await msg.answer("Vazifa yozing: /task Kitob o‘qish")

    pool = await create_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            "INSERT INTO tasks (user_id, title) VALUES ($1, $2)",
            msg.from_user.id, title
        )

    await msg.answer("✅ Vazifa qo‘shildi.")
