# cogs/core.py

import discord
from discord.ext import commands, tasks
import datetime

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder_loop.start()

    # A custom help command
    @commands.command(name="help")
    async def help_command(self, ctx):
        help_text = """**Help Menu**:
        `!help` - Show this help message
        `!ping` - Check if the bot is alive
        ...
        More commands are available by checking each category.
        """
        await ctx.send(help_text)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Welcome message in a specific channel
        welcome_channel = discord.utils.get(member.guild.channels, name="general")
        if welcome_channel:
            await welcome_channel.send(f"Welcome {member.mention} to **{member.guild.name}**!")
        # You can also DM the user
        try:
            await member.send(f"Hello {member.name}, welcome to **{member.guild.name}**!")
        except:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Log that a member has left
        print(f"{member} has left {member.guild.name}")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        # Log deleted message
        print(f"Message deleted: {message.content} by {message.author}")

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Check the bot's latency."""
        latency = self.bot.latency
        await ctx.send(f"Pong! Latency: {latency*1000:.2f}ms")

    @tasks.loop(minutes=1.0)
    async def reminder_loop(self):
        # This is a scheduled loop that runs every minute
        # You could check a database or file for scheduled announcements
        # Example: send reminders at a specific time
        current_time = datetime.datetime.now().strftime('%H:%M')
        # Example: if it's 09:00, do something
        if current_time == "09:00":
            # broadcast message logic
            pass

    @reminder_loop.before_loop
    async def before_reminder_loop(self):
        # Wait until the bot is ready
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Core(bot))
