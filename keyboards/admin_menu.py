from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Statistika")],
        [KeyboardButton(text="Foydalanuvchilar")]
    ],
    resize_keyboard=True
)
