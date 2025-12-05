import asyncio
from datetime import datetime
from database import create_pool

async def send_reminders(bot):
    pool = await create_pool()

    async with pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT user_id, text FROM reminders WHERE remind_at <= NOW()"
        )

    for row in rows:
        try:
            await bot.send_message(row["user_id"], f"🔔 Eslatma: {row['text']}")
        except Exception as e:
            print("Xato:", e)


async def start_scheduler(bot):
    while True:
        await send_reminders(bot)
        await asyncio.sleep(60)   # har 1 daqiqada tekshiradi
