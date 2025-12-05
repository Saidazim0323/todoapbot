# main.py
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from routers.admin import admin_router
from routers.habit import habit_router
from routers.reminder import reminder_router
from database import connect_db

# --- Environment variables ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# --- Bot va Dispatcher ---
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- Routers qo'shish ---
dp.include_router(admin_router)
dp.include_router(habit_router)
dp.include_router(reminder_router)

# --- Admin panel ---
# routers/admin.py
from aiogram import Router, types

admin_router = Router()

@admin_router.message(lambda m: hasattr(m.from_user, 'id') and m.from_user.id == ADMIN_ID)
async def admin_panel(msg: types.Message):
    await msg.answer("🔐 Admin paneliga xush kelibsiz!")

# --- Habit qo'shish ---
# routers/habit.py
from aiogram import Router, types
from database import connect_db

habit_router = Router()

@habit_router.message(Command("habit"))
async def add_habit(msg: types.Message):
    habit = msg.text.replace("/habit", "").strip()
    if not habit:
        await msg.answer("❌ Iltimos, odatingizni yozing. Masalan: /habit Meditatsiya")
        return

    try:
        conn = await connect_db()
        await conn.execute(
            "INSERT INTO habits (user_id, habit) VALUES ($1,$2)",
            msg.from_user.id, habit
        )
    finally:
        await conn.close()

    await msg.answer(f"💪 Odatingiz qo‘shildi: {habit}")

# --- Reminder vaqti o'rnatish ---
# routers/reminder.py
from aiogram import Router, types
from database import connect_db

reminder_router = Router()

@reminder_router.message(Command("time"))
async def set_time(msg: types.Message):
    try:
        hour = int(msg.text.split()[1])
        if not 0 <= hour <= 23:
            await msg.answer("0-23 oralig‘ida soat kiriting.")
            return
    except (IndexError, ValueError):
        await msg.answer("To‘g‘ri format: /time 9 (misol)")
        return

    try:
        conn = await connect_db()
        await conn.execute(
            "UPDATE users SET reminder_hour=$1 WHERE user_id=$2",
            hour, msg.from_user.id
        )
    finally:
        await conn.close()

    await msg.answer(f"🔔 Eslatma vaqti o‘rnatildi: {hour}:00")

# --- Main polling ---
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
