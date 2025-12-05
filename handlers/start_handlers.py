# handlers/start_handlers.py
from aiogram import Router, types
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def start_cmd(msg: types.Message):
    await msg.answer("👋 Assalomu alaykum! Men ishlayapman.")
    

def register_start_handlers(dp):
    dp.include_router(start_router)
