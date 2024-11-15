from pyrogram import Client, filters
from Helpo import Helpo

app = Client("my_bot")

pagination = Helpo(app, "Bot/modules")


@app.on_message(filters.command("afk"))
async def afk_command(client, message):
    await message.reply("You are now AFK.")


# No Need to Add callback query 
@app.on_message(filters.command("start"))
async def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Help", callback_data="global_help")]
    ])
    await message.reply("Welcome! Click the button below for help.", reply_markup=keyboard)


app.run()

print("Example usage module loaded")

__HELP__ = """
1) /afk - Set user as AFK
"""

__MODULE__ = "AFK"
