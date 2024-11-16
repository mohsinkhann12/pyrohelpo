# Helpo 📚

A powerful and flexible pagination library for Pyrogram bots that automatically handles help commands and module organization.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features ✨

- 🔄 Automatic module discovery and help text organization
- 📱 Beautiful paginated help menus with inline buttons
- 🎯 Support for both command-based and button-based help
- 🎨 Customizable button layouts (6 buttons per page)
- 🔌 Easy integration with existing Pyrogram bots
- 📝 Support for rich media in help messages (photos, videos)

## Installation 🚀

```bash
pip install Helpo
```

## Usage ⚙️

# Initialise the instance 

```python

from Helpo import Helpo

custom_texts = {
    "help_menu_title": "**🛠 Custom Help Menu**",
    "help_menu_intro": "Available modules ({count}):\n{modules}\n\nTap on a module to explore.",
    "module_help_title": "**🔍 Details for {module_name} Module**",
    "module_help_intro": "Description:\n{help_text}",
    "no_modules_loaded": "⚠️ No modules available at the moment.",
    "back_button": "◀️ Go Back",
    "prev_button": "⬅️ Previous Page",
    "next_button": "➡️ Next Page",
    "support_button": "💬 Contact Support",
    "support_url": "https://t.me/YourSupportBot",
}

pagination = Helpo(
    client=bot,
    modules_path="fwd/plugins",
    buttons_per_page=9,
    texts=custom_texts,
    help_var="HELP",
    module_var="MODULE",
)
```

##  setup help and module for each py file present in modules path

```python

MODULE = "HELPO"

HELP = "GO GOA GONE" # you can use docs strings too

```

## using custom class 

```python

custom_texts = {
    "help_menu_title": "**?? Custom Help Menu**",
    "help_menu_intro": "Available modules ({count}):\n{modules}\n\nTap on
a module for more details.",
    "module_help_title": "**?? Details for {module_name} Module**",
    "module_help_intro": "Description:\n{help_text}",
    "no_modules_loaded": "⚠️ No modules available at the moment.",
    "back_button": "◀️ Go Back",
    "prev_button": "⬅️ Previous Page",
    "next_button": "➡️ Next Page",
    "support_button": "?? Contact Support",
    "support_url": "https://t.me/YourSupportBot",
}
class Bot(Client):
    def __init__(self):
        super().__init__(
            "Hoshi-new",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            plugins=dict(root="shivu"),
        )
        self.helpo = Helpo(
            client=self,
            modules_path="shivu/modules",
            buttons_per_page=6,
            texts=custom_texts,
        )
    async def start(self):
        await super().start()
        LOGGER.info("Pyro Bot Started")
        LOGGER.info("Helpo Initialized with Modules: %s", ", ".join(self.helpo.modules.keys()))
    async def stop(self):
        await super().stop()
        LOGGER.info("Pyro Bot Stopped")
```

## for deep linking 

```python

@bot.on_message(filters.command("start"))
async def start_commandd(client, message):
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name.startswith("help"):
            await bot.show_help_menu(message.chat.id, page=1)
```

## for help as button anywhere without callback query 

```python
 
from . import pagination # import your Helpo Instance 


@bot.on_message(filters.command("start"))
async def start_commandd(client, message):
    keyboard = InlineKeyboardMarkup([
         [InlineKeyboardButton("Help", callback_data="global_help")]
         ])
        await message.reply("Welcome! Click the button below for help.", reply_markup=keyboard)
```

