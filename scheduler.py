import asyncio
from database import connect_db
from aiogram import Bot
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

async def send_daily_reminders():
    while True:
        conn = await connect_db()
        users = await conn.fetch("SELECT user_id, reminder_hour FROM users")
        await conn.close()

        from datetime import datetime
        now_hour = datetime.now().hour

        for u in users:
            if u["reminder_hour"] == now_hour:
                try:
                    await bot.send_message(u["user_id"], "⏰ Eslatma! Vazifalaringizni tekshiring.")
                except:
                    pass

        await asyncio.sleep(3600)
