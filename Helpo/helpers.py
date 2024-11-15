from typing import List
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def chunk_list(lst: List, n: int) -> List[List]:
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def create_pagination_keyboard(modules: List[str], current_page: int, total_pages: int, texts: dict) -> InlineKeyboardMarkup:
    keyboard = []
    for i in range(0, len(modules), 3):
        row = [InlineKeyboardButton(m, callback_data=f"help_module_{m}") for m in modules[i:i + 3]]
        keyboard.append(row)

    nav_row = []
    if total_pages > 1:
        nav_row.append(InlineKeyboardButton(texts["prev_button"], callback_data=f"help_prev_{current_page}"))
    nav_row.append(InlineKeyboardButton(texts["support_button"], url=texts["support_url"]))
    if total_pages > 1:
        nav_row.append(InlineKeyboardButton(texts["next_button"], callback_data=f"help_next_{current_page}"))

    keyboard.append(nav_row)
    return InlineKeyboardMarkup(keyboard)
