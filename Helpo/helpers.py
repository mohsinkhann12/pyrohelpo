from typing import List
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def chunk_list(lst: List, n: int) -> List[List]:
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def create_pagination_keyboard(modules: List[str], current_page: int, total_pages: int) -> InlineKeyboardMarkup:
    keyboard = []
    for i in range(0, len(modules), 3):
        row = [InlineKeyboardButton(m, callback_data=f"help_module_{m}") for m in modules[i:i+3]]
        keyboard.append(row)
    
    nav_row = []
    if total_pages > 1:
        nav_row.append(InlineKeyboardButton("⬅️ Previous", callback_data=f"help_prev_{current_page}"))
    nav_row.append(InlineKeyboardButton("👥 Support", url="https://t.me/Xlzeo"))
    if total_pages > 1:
        nav_row.append(InlineKeyboardButton("Next ➡️", callback_data=f"help_next_{current_page}"))
    
    keyboard.append(nav_row)
    return InlineKeyboardMarkup(keyboard)

print("Helpo helpers module loaded")
