# cogs/fun.py

import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.jokes = [
            "Why did the chicken join a band? Because it had the drumsticks!",
            "What's orange and sounds like a parrot? A carrot!"
        ]
        self.quotes = [
            "Be yourself; everyone else is already taken. — Oscar Wilde",
            "In the end, we only regret the chances we didn't take. — Lewis Carroll"
        ]

    @commands.command(name="joke")
    async def tell_joke(self, ctx):
        """Tell a random joke."""
        await ctx.send(random.choice(self.jokes))

    @commands.command(name="quote")
    async def send_quote(self, ctx):
        """Send a random quote."""
        await ctx.send(random.choice(self.quotes))

    @commands.command(name="meme")
    async def generate_meme(self, ctx):
        """Placeholder for a Meme generator command."""
        await ctx.send("Meme generator not fully implemented yet!")

    @commands.command(name="8ball")
    async def eight_ball(self, ctx, *, question):
        """Magic 8-ball for fortune telling."""
        responses = [
            "It is certain.",
            "Outlook not so good.",
            "Ask again later.",
            "Yes, definitely."
        ]
        answer = random.choice(responses)
        await ctx.send(f"**Question:** {question}\n**Answer:** {answer}")

async def setup(bot):
    await bot.add_cog(Fun(bot))
