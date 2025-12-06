import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiohttp import web

from config import BOT_TOKEN, WEBHOOK_URL
from database import create_tables

from handlers.start_handlers import register_start_handlers
from handlers.admin_handlers import register_admin_handlers
from handlers.task_handlers import register_task_handlers
from handlers.habit_handlers import register_habit_handlers
from handlers.reminder_handlers import register_reminder_handlers
from scheduler import start_scheduler

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def register_all_handlers():
    register_start_handlers(dp)
    register_admin_handlers(dp)
    register_task_handlers(dp)
    register_habit_handlers(dp)
    register_reminder_handlers(dp)


async def webhook_handler(request):
    data = await request.json()
    update = Update(**data)
    await dp.feed_update(bot, update)
    return web.Response(text="OK")


async def on_startup(app):
    register_all_handlers()
    await create_tables()   # <-- jadval yaratish
    await bot.set_webhook(WEBHOOK_URL)
    asyncio.create_task(start_scheduler(bot))


def main():
    app = web.Application()
    app.router.add_post("/", webhook_handler)
    app.on_startup.append(on_startup)
    port = int(os.getenv("PORT", 8000))
    web.run_app(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
