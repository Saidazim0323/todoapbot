import asyncio
from datetime import datetime
from database import get_db

async def send_reminders(bot):
    db = await get_db()
    rows = await db.fetch("SELECT user_id, text FROM reminders WHERE remind_at <= NOW()")
    for row in rows:
        try:
            await bot.send_message(row["user_id"], f"🔔 Eslatma: {row['text']}")
        except:
            pass

async def start_scheduler(bot):
    while True:
        await send_reminders(bot)
        await asyncio.sleep(60)
