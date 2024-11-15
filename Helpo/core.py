import os
import importlib
from typing import List, Dict, Any
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from Helpo.helpers import chunk_list, create_pagination_keyboard

class Helpo:
    def __init__(self, client: Client, modules_path: str):
        self.client = client
        self.modules_path = modules_path
        self.modules: Dict[str, Dict[str, Any]] = {}
        self.load_modules()
        self.monkeypatch_client()

    def load_modules(self):
        for filename in os.listdir(self.modules_path):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]
                module = importlib.import_module(f"{self.modules_path.replace('/', '.')}.{module_name}")
                if hasattr(module, '__MODULE__') and hasattr(module, '__HELP__'):
                    self.modules[module.__MODULE__] = {
                        'name': module.__MODULE__,
                        'help': module.__HELP__
                    }
        print(f"Loaded {len(self.modules)} modules: {', '.join(self.modules.keys())}")

    def monkeypatch_client(self):
        @self.client.on_message(filters.command("help"))
        async def help_command(client, message):
            await self.show_help_menu(message.chat.id)

        @self.client.on_callback_query(filters.regex(r'^help_'))
        async def help_button(client, callback_query: CallbackQuery):
            data = callback_query.data.split('_')
            if data[1] == 'module':
                await self.show_module_help(callback_query, data[2])
            elif data[1] in ['next', 'prev']:
                page = int(data[2])
                if data[1] == 'next':
                    page += 1
                else:
                    page -= 1
                await self.show_help_menu(callback_query.message.chat.id, page, callback_query.message.id)
            elif data[1] == 'back':
                await self.show_help_menu(callback_query.message.chat.id, message_id=callback_query.message.id)

    async def show_help_menu(self, chat_id: int, page: int = 1, message_id: int = None):
        modules_list = list(self.modules.keys())
        chunks = list(chunk_list(modules_list, 6))
        
        if not chunks:
            text = "No modules loaded."
            keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("👥 Support", url="https://t.me/Xlzeo")]])
        else:
            if page > len(chunks):
                page = 1
            elif page < 1:
                page = len(chunks)
            
            keyboard = create_pagination_keyboard(chunks[page-1], page, len(chunks))
            
            text = f"**📚 Help Menu**\n\nLoaded {len(self.modules)} modules: {', '.join(self.modules.keys())}\n\nClick on a module to see its help message."
        
        if message_id:
            await self.client.edit_message_text(chat_id, message_id, text, reply_markup=keyboard)
        else:
            await self.client.send_message(chat_id, text, reply_markup=keyboard)

    async def show_module_help(self, callback_query: CallbackQuery, module_name: str):
        module = self.modules.get(module_name)
        if module:
            text = f"**📘 {module['name']} Module**\n\n{module['help']}"
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="help_back")]
            ])
            await callback_query.edit_message_text(text, reply_markup=keyboard)
        else:
            await callback_query.answer("Module not found!", show_alert=True)

    async def global_help(self, chat_id: int, message_id: int):
        await self.show_help_menu(chat_id, message_id=message_id)

print("Helpo core module loaded")
