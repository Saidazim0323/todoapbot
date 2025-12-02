from aiogram import Router, types
from database import connect_db

reminder_router = Router()

@reminder_router.message(commands=["time"])
async def set_time(msg: types.Message):
    try:
        hour = int(msg.text.split()[1])
        if hour < 0 or hour > 23:
            return await msg.answer("0-23 oralig‘ida soat kiriting.")
    except:
        return await msg.answer("/time 9 (misol)")

    conn = await connect_db()
    await conn.execute("UPDATE users SET reminder_hour=$1 WHERE user_id=$2",
                       hour, msg.from_user.id)
    await conn.close()

    await msg.answer(f"🔔 Eslatma vaqti o‘rnatildi: {hour}:00")
