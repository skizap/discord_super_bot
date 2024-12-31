# cogs/games.py

import discord
from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rps")
    async def rock_paper_scissors(self, ctx, choice: str):
        """Play Rock Paper Scissors."""
        rps_choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(rps_choices)
        player_choice = choice.lower()

        if player_choice not in rps_choices:
            await ctx.send("Please choose rock, paper, or scissors.")
            return

        await ctx.send(f"I chose {bot_choice}!")
        if player_choice == bot_choice:
            await ctx.send("It's a tie!")
        elif (player_choice == "rock" and bot_choice == "scissors") or \
             (player_choice == "paper" and bot_choice == "rock") or \
             (player_choice == "scissors" and bot_choice == "paper"):
            await ctx.send("You win!")
        else:
            await ctx.send("You lose!")

    @commands.command(name="slots")
    async def slot_machine(self, ctx):
        """Simple slot machine."""
        symbols = ["🍒", "🍋", "🍊", "🍀", "⭐", "7️⃣"]
        result = [random.choice(symbols) for _ in range(3)]
        result_str = " | ".join(result)
        await ctx.send(f"**[ {result_str} ]**")

        # Basic check if all match
        if len(set(result)) == 1:
            await ctx.send("JACKPOT! You won!!")
        else:
            await ctx.send("Better luck next time.")

    @commands.command(name="trivia")
    async def trivia_game(self, ctx):
        """Placeholder for Trivia game."""
        await ctx.send("Trivia game not fully implemented yet.")

    @commands.command(name="fish")
    async def fish_game(self, ctx):
        """Fishing simulation placeholder."""
        fish_types = ["Salmon", "Trout", "Shark", "Tuna"]
        catch = random.choice(fish_types)
        await ctx.send(f"You cast your line and caught a **{catch}**!")

async def setup(bot):
    await bot.add_cog(Games(bot))
