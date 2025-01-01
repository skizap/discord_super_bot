# cogs/economy.py

import discord
from discord.ext import commands
import datetime
import random

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_balances = {}  # In production, store this in a database
        self.last_daily_claim = {}  # Track daily reward cooldown

    def get_balance(self, user_id):
        return self.user_balances.get(user_id, 0)

    def set_balance(self, user_id, amount):
        self.user_balances[user_id] = amount

    @commands.command(name="balance")
    async def check_balance(self, ctx):
        bal = self.get_balance(ctx.author.id)
        await ctx.send(f"Your current balance is: {bal} coins")

    @commands.command(name="daily")
    async def daily_reward(self, ctx):
        user_id = ctx.author.id
        now = datetime.datetime.now()
        last_claim = self.last_daily_claim.get(user_id, None)
        if last_claim and (now - last_claim).days < 1:
            await ctx.send("You have already claimed your daily reward. Try again tomorrow.")
        else:
            reward = random.randint(50, 100)
            new_bal = self.get_balance(user_id) + reward
            self.set_balance(user_id, new_bal)
            self.last_daily_claim[user_id] = now
            await ctx.send(f"You claimed {reward} coins! Your new balance is {new_bal} coins.")

    @commands.command(name="gamble")
    async def gamble_coins(self, ctx, amount: int):
        user_id = ctx.author.id
        bal = self.get_balance(user_id)
        if amount <= 0:
            await ctx.send("You must gamble a positive amount.")
            return
        if bal < amount:
            await ctx.send("You don't have enough coins!")
            return
        # 50/50 chance
        if random.choice([True, False]):
            bal += amount
            await ctx.send(f"You won {amount} coins! New balance is {bal}.")
        else:
            bal -= amount
            await ctx.send(f"You lost {amount} coins! New balance is {bal}.")
        self.set_balance(user_id, bal)

async def setup(bot):
    await bot.add_cog(Economy(bot))
