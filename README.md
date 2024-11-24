# Helpo 📚

![Image](https://socialify.git.ci/Vishal-1756/pyrohelpo/image?description=1&font=KoHo&name=1&owner=1&pattern=Charlie%20Brown&theme=Dark)

A powerful and flexible pagination library for Pyrogram bots that automatically handles help commands and module organization.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![PyPI Downloads](https://static.pepy.tech/badge/pyrohelpo)

## Features ✨

- 🔄 Automatic module discovery and help text organization
- 📱 Beautiful paginated help menus with inline buttons
- 🎯 Support for both command-based and button-based help
- 🎨 Customizable button layouts and texts
- 🔌 Easy integration with existing Pyrogram bots
- 📝 Support for rich media in help messages (photos, videos)
- 🔗 Deep linking support for direct access to help menus
- 🌐 Group chat support with private message options
- 🎭 Flexible parse mode selection
- 🖼️ Media support with photo and video options

## Installation 🚀

```bash
pip install pyrohelpo
```

## Usage ⚙️

### Basic Setup

```python
from pyrogram import Client
from Helpo import Helpo
from pyrogram.enums import ParseMode

# Initialize your Pyrogram client
app = Client("my_bot")

# Initialize Helpo
helpo = Helpo(
    client=app,
    modules_path="plugins",
    buttons_per_page=6
)
```

### Advanced Configuration

```python
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
    "group_help_message": "Click The Button To Access Help",
    "group_pvt_button": "See In Private",
    "group_open_here": "Open Here"
}

helpo = Helpo(
    client=app,
    modules_path="plugins",
    buttons_per_page=6,
    texts=custom_texts,
    help_var="HELP",
    module_var="MODULE",
    photo="path/to/photo.jpg",  # Optional: Add photo to help messages
    video="path/to/video.mp4",  # Optional: Add video to help messages
    parse_mode=ParseMode.HTML,  # Optional: Change parse mode (default: MARKDOWN)
    disable_web_page_preview=False  # Optional: Enable web preview (default: True)
)
```

### Module Setup

Create Python files in your modules directory with the following structure:

```python
MODULE = "Admin"  # Module name displayed in help menu
HELP = """
**Admin Commands**
/ban - Ban a user
/unban - Unban a user
/mute - Mute a user
/unmute - Unmute a user
"""
```

### Custom Class Implementation

```python
class Bot(Client):
    def __init__(self):
        super().__init__(
            "my_bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN
        )
        self.helpo = Helpo(
            client=self,
            modules_path="plugins",
            buttons_per_page=6,
            texts=custom_texts
        )

    async def start(self):
        await super().start()
        print("Bot Started")
        print(f"Loaded Modules: {', '.join(self.helpo.modules.keys())}")

    async def stop(self):
        await super().stop()
        print("Bot Stopped")
```

### Group Chat Support

The new Helpo version automatically handles group chats by providing options to:

- View help menu in private chat
- View help menu directly in the group
- Customize group chat behavior through texts dictionary


### Deep Linking Support

```python
@app.on_message(filters.command("start"))
async def start_command(client, message):
    if len(message.text.split()) > 1:
        param = message.text.split(None, 1)[1]
        if param == "help":
            await client.show_help_menu(message.chat.id)
    else:
        await message.reply("Welcome! Use /help to see available commands.")
```

## Customization Options 🎨

### Available Text Customizations

All text elements can be customized through the `texts` dictionary:

- `help_menu_title`: Title of the main help menu
- `help_menu_intro`: Introduction text with module count
- `module_help_title`: Title for individual module help
- `module_help_intro`: Introduction text for module help
- `no_modules_loaded`: Message when no modules are found
- `back_button`: Text for back button
- `prev_button`: Text for previous page button
- `next_button`: Text for next page button
- `support_button`: Text for support button
- `support_url`: URL for support button
- `group_help_message`: Message shown in groups
- `group_pvt_button`: Text for private chat button
- `group_open_here`: Text for in-group help button


### Media Support

You can enhance your help menu with either photos or videos:

```python
helpo = Helpo(
    client=app,
    modules_path="plugins",
    photo="https://example.com/help-banner.jpg"  # OR
    video="https://example.com/help-tutorial.mp4"
)
```

Note: You can only use either photo or video, not both simultaneously.

## Methods and Attributes 📚

### Helpo Class

#### Attributes:

- `client`: Pyrogram Client instance
- `modules_path`: Path to modules directory
- `buttons_per_page`: Number of buttons per page
- `help_var`: Variable name for help text (default: "**HELP**")
- `module_var`: Variable name for module name (default: "**MODULE**")
- `photo`: Optional photo URL/path
- `video`: Optional video URL/path
- `parse_mode`: Message parse mode
- `disable_web_page_preview`: Web preview setting
- `texts`: Customizable text dictionary


#### Methods:

- `load_modules()`: Loads all modules from the specified path
- `show_help_menu()`: Displays the main help menu
- `show_module_help()`: Shows help for a specific module


## Error Handling

Helpo includes comprehensive error handling for:

- Invalid module files
- Missing required attributes
- Media loading failures
- Message sending errors
- Callback query processing


## Contributors 👥

- [vishal-1756](https://github.com/vishal-1756)
- [siyu-xd](https://github.com/siyu-xd)


## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 🤝

Need help? Join our [support chat](https://t.me/Blank_Advice) or create an issue on our [GitHub repository](https://github.com/Vishal-1756/Helpo).

## Image Gallery 🖼️

---

Made with ❤️ by the Helpo team
