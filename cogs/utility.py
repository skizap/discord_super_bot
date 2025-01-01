# cogs/utility.py

import discord
from discord.ext import commands
import requests
import math

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="weather")
    async def weather(self, ctx, *, city: str):
        """Get weather (placeholder; you need an API key for a real implementation)."""
        await ctx.send(f"Weather in {city}: Data not implemented. (Use OpenWeatherMap API, etc.)")

    @commands.command(name="crypto")
    async def crypto_price(self, ctx, *, symbol: str):
        """Get cryptocurrency price (placeholder)."""
        symbol = symbol.upper()
        # Example call to a crypto API (like CoinGecko or Binance)
        await ctx.send(f"Price of {symbol}: Not implemented. (Fetch via an API.)")

    @commands.command(name="poll")
    async def create_poll(self, ctx, *, question):
        """Create a poll with reactions."""
        poll_message = await ctx.send(f"**Poll:** {question}")
        await poll_message.add_reaction("👍")
        await poll_message.add_reaction("👎")

    @commands.command(name="shorten")
    async def shorten_url(self, ctx, *, url: str):
        """URL shortener (placeholder)."""
        await ctx.send(f"Shortened URL of {url}: Not implemented. (Use bitly or tinyurl API.)")

    @commands.command(name="calc")
    async def calculator(self, ctx, *, expression):
        """Simple math calculator using Python's eval. (Be VERY careful with eval in production!)"""
        try:
            result = eval(expression)
            await ctx.send(f"{expression} = {result}")
        except:
            await ctx.send("Invalid expression.")

    @commands.command(name="backup_server")
    @commands.has_permissions(administrator=True)
    async def backup_server(self, ctx):
        """Server backup placeholder."""
        # Real backups would store roles, channels, permissions, etc.
        await ctx.send("Server backup not fully implemented yet. Would store roles/channels/settings.")

async def setup(bot):
    await bot.add_cog(Utility(bot))
