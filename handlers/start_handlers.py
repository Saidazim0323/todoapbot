from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

def register_start_handlers(dp):
    dp.include_router(start_router)

@start_router.message(Command("start"))
async def start_cmd(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="/task"), types.KeyboardButton(text="/habit")],
            [types.KeyboardButton(text="/admin"), types.KeyboardButton(text="/time")]
        ],
        resize_keyboard=True
    )

    await msg.answer("📌 Menyudan birini tanlang:", reply_markup=keyboard)
