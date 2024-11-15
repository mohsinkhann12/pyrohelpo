import os
import importlib
from typing import List, Dict, Any
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from Helpo.helpers import chunk_list, create_pagination_keyboard


class Helpo:
    def __init__(self, client: Client, modules_path: str, buttons_per_page: int = 6, help_var: str = "__HELP__", module_var: str = "__MODULE__"):
        self.client = client
        self.modules_path = modules_path
        self.buttons_per_page = buttons_per_page
        self.help_var = help_var
        self.module_var = module_var
        self.modules: Dict[str, Dict[str, Any]] = {}
        self.load_modules()
        self.monkeypatch_client()

    def load_modules(self):
        for filename in os.listdir(self.modules_path):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]
                module = importlib.import_module(f"{self.modules_path.replace('/', '.')}.{module_name}")
                if hasattr(module, self.module_var) and hasattr(module, self.help_var):
                    self.modules[getattr(module, self.module_var, module_name)] = {
                        'name': getattr(module, self.module_var, module_name),
                        'help': getattr(module, self.help_var, "No help available for this module.")
                    }
        print(f"Loaded {len(self.modules)} modules: {', '.join(self.modules.keys())}")

    def monkeypatch_client(self):
        @self.client.on_message(filters.command("help"))
        async def help_command(client, message):
            await self.show_help_menu(message.chat.id)

        @self.client.on_message(filters.command("start"))
        async def start_command(client, message):
            if len(message.text.split()) >1:
                name = message.text.split(None, 1)[1]
                if name[0:4] == "help":
                    await self.show_help_menu(message.chat.id)
            else:
                pass

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

        @self.client.on_callback_query(filters.regex(r'^global_help$'))
        async def global_help(client, callback_query: CallbackQuery):
            await self.show_help_menu(callback_query.message.chat.id, message_id=callback_query.message.id)

    async def show_help_menu(self, chat_id: int, page: int = 1, message_id: int = None):
        modules_list = list(self.modules.keys())
        chunks = list(chunk_list(modules_list, self.buttons_per_page))
        
        if not chunks:
            text = "No modules loaded."
            keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("👥 Support", url="https://t.me/Xlzeo")]])
        else:
            if page > len(chunks):
                page = 1
            elif page < 1:
                page = len(chunks)
            
            keyboard = create_pagination_keyboard(chunks[page-1], page, len(chunks))
            
            text = f"**📚 Help Menu**\n\nLoaded {len(self.modules)} modules:\n{', '.join(self.modules.keys())}\n\nClick on a module to see its help message."
        
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


print("Helpo core module loaded")
