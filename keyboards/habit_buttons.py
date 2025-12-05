from aiogram.utils.keyboard import InlineKeyboardBuilder

def habit_buttons():
    kb = InlineKeyboardBuilder()
    kb.button(text="➕ Odat qo‘shish", callback_data="add_habit")
    return kb.as_markup()
