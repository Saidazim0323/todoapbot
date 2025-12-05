from aiogram.utils.keyboard import InlineKeyboardBuilder

def task_buttons():
    kb = InlineKeyboardBuilder()
    kb.button(text="➕ Qo‘shish", callback_data="add_task")
    return kb.as_markup()
