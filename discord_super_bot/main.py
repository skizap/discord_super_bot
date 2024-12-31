# main.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Intents (we need these for various events like member join, message edit, reaction events, etc.)
intents = discord.Intents.all()

# Create the bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None  # We can implement a custom help command
)

# List of initial cogs to load
INITIAL_COGS = [
    "cogs.core",
    "cogs.moderation",
    "cogs.music",
    "cogs.fun",
    "cogs.games",
    "cogs.utility",
    "cogs.economy",
    "cogs.roleplay"
    # Add more cogs if desired
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    # You can set a custom status
    await bot.change_presence(activity=discord.Game("Ultimate Discord Bot!"))

# Load all cogs
def load_cogs():
    for cog in INITIAL_COGS:
        try:
            bot.load_extension(cog)
            print(f"Loaded cog: {cog}")
        except Exception as e:
            print(f"Failed to load cog {cog}: {e}")

if __name__ == "__main__":
    load_cogs()
    bot.run(TOKEN)
