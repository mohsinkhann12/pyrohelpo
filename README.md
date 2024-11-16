# Helpo 📚

A powerful and flexible pagination library for Pyrogram bots that automatically handles help commands and module organization.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features ✨

- 🔄 Automatic module discovery and help text organization
- 📱 Beautiful paginated help menus with inline buttons
- 🎯 Support for both command-based and button-based help
- 🎨 Customizable button layouts and texts
- 🔌 Easy integration with existing Pyrogram bots
- 📝 Support for rich media in help messages (photos, videos)
- 🔗 Deep linking support for direct access to help menus

## Installation 🚀

```bash
pip install pyrohelpo
```

## Usage ⚙️

### Initialize the Helpo instance

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

### Set up help and module for each Python file in the modules path

```python
MODULE = "HELPO"

HELP = "GO GOA GONE"  # You can use docstrings too
```

### Using a custom class

```python
from pyrogram import Client
from Helpo import Helpo

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
        print("Pyro Bot Started")
        print(f"Helpo Initialized with Modules: {', '.join(self.helpo.modules.keys())}")

    async def stop(self):
        await super().stop()
        print("Pyro Bot Stopped")
```

### Deep linking support

```python
@bot.on_message(filters.command("start"))
async def start_command(client, message):
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name.startswith("help"):
            await bot.show_help_menu(message.chat.id, page=1)
```

### Adding a help button anywhere without callback query

```python
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from . import pagination  # Import your Helpo instance

@bot.on_message(filters.command("start"))
async def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Help", callback_data="global_help")]
    ])
    await message.reply("Welcome! Click the button below for help.", reply_markup=keyboard)
```

## Customization Options 🎨

Helpo offers various customization options to tailor the help menu to your bot's needs:

- `buttons_per_page`: Set the number of buttons displayed per page (default: 6)
- `texts`: Customize all text messages and button labels
- `help_var` and `module_var`: Set custom variable names for help text and module names
- `photo` and `video`: Add rich media to your help messages
- `parse_mode`: Set the parse mode for help messages (default: ParseMode.MARKDOWN)
- `disable_web_page_preview`: Enable or disable web page previews in help messages

# Image Gallery 

<details>
<summary>Help menu using video</summary>

![Help menu using video](https://i.ibb.co/W6GSqRx/b8a4679a3f10.jpg)
Description: This menu displays video tutorials to help users.

</details>

<details>
<summary>Help menu using only text</summary>

![Help menu using only text](https://i.ibb.co/Ct5P1jQ/68a1de1130d3.jpg)
Description: This menu uses text-based instructions for simplicity.

</details>

<details>
<summary>Help menu using photo</summary>

![Help menu using photo](https://i.ibb.co/H70SLgQ/741d52da8c46.jpg)
Description: This menu uses images to visually assist users.

</details>

<details>
<summary>Help menu of a module</summary>

![Help menu of a module](https://i.ibb.co/BzFD1kj/ad4c32676c6e.jpg)
Description: This menu shows a module-specific help interface.

</details>

## Methods and Attributes 📚

### Helpo Class

#### Attributes:
- `client`: The Pyrogram Client instance
- `modules_path`: Path to the modules directory
- `buttons_per_page`: Number of buttons per page in the help menu
- `help_var`: Variable name for help text in modules
- `module_var`: Variable name for module name in modules
- `photo`: Optional photo to be used in help messages
- `video`: Optional video to be used in help messages
- `parse_mode`: Parse mode for help messages
- `disable_web_page_preview`: Whether to disable web page previews in help messages
- `texts`: Dictionary of customizable text strings

### Error Handling

Helpo includes error handling for various scenarios:
- Invalid module files
- Missing required attributes in modules
- Failed module loading
- Message sending failures

## Contributors 👥

- [vishal-1756](https://github.com/vishal-1756)
- [siyu-xd](https://github.com/siyu-xd)

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 🤝

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/Vishal-1756/Helpo) or join our [support chat](https://t.me/Blank_Advice).

## Acknowledgements 🙏

- [Pyrogram](https://docs.pyrogram.org/) - The awesome MTProto library for Python
- All contributors who have helped this project grow

---

Made with ❤️ by the Helpo team

