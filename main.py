import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from config import BOT_TOKEN, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT
from handlers.admin_handlers import admin_router
from handlers.task_handlers import task_router
from handlers.habit_handlers import habit_router
from handlers.reminder_handlers import reminder_router
from scheduler import send_daily_reminders
from database import create_tables

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(admin_router)
dp.include_router(task_router)
dp.include_router(habit_router)
dp.include_router(reminder_router)


async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    await create_tables()
    asyncio.create_task(send_daily_reminders())


async def on_shutdown(app):
    await bot.delete_webhook()


async def main():
    app = web.Application()
    webhook_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_handler.register(app, path="/webhook")
    setup_application(app, dp, bot=bot)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)


if __name__ == "__main__":
    asyncio.run(main())
