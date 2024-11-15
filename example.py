from pyrogram import Client, filters
from Helpo import Helpo, module_help

app = Client("my_bot")
pagination = PyroPagination(app, "Bot/modules")

@module_help("AFK")
@app.on_message(filters.command("afk"))
async def afk_command(client, message):
    # Your AFK command logic here
    await message.reply("You are now AFK.")

__HELP__ = """
1) /afk - Set user as AFK
"""

@app.on_message(filters.command("start"))
async def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Help", callback_data="global_help")]
    ])
    await message.reply("Welcome! Click the button below for help.", reply_markup=keyboard)

@app.on_callback_query(filters.regex("^global_help$"))
async def global_help_button(client, callback_query):
    await pagination.global_help(callback_query.message.chat.id, callback_query.message.id)

app.run()

print("Example usage module loaded")
