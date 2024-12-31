# cogs/moderation.py

import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spam_threshold = 5  # number of messages in a time window
        self.user_message_count = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # Basic spam detection
        user_id = message.author.id
        self.user_message_count.setdefault(user_id, 0)
        self.user_message_count[user_id] += 1

        if self.user_message_count[user_id] > self.spam_threshold:
            # Take action: e.g., mute or warn
            await message.channel.send(f"Please stop spamming, {message.author.mention}!")
            # Reset their count
            self.user_message_count[user_id] = 0

        # Filter inappropriate content example
        banned_words = ["badword1", "badword2", "badword3"]
        for word in banned_words:
            if word in message.content.lower():
                await message.delete()
                await message.channel.send(f"Inappropriate word used by {message.author.mention}.")
                return

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick_member(self, ctx, member: discord.Member, *, reason=None):
        """Kick a member from the server."""
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked. Reason: {reason}")

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban_member(self, ctx, member: discord.Member, *, reason=None):
        """Ban a member from the server."""
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned. Reason: {reason}")

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban_member(self, ctx, *, member_name):
        """Unban a member by name."""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member_name.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @commands.command(name="create_ticket")
    async def create_ticket(self, ctx):
        """A simple ticket system example."""
        # Create a new channel for the ticket
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)
        }
        ticket_channel = await guild.create_text_channel(
            name=f"ticket-{ctx.author.name}",
            overwrites=overwrites
        )
        await ticket_channel.send(f"Ticket created by {ctx.author.mention}")

    @commands.command(name="close_ticket")
    @commands.has_permissions(manage_channels=True)
    async def close_ticket(self, ctx):
        """Close the current ticket channel."""
        if ctx.channel.name.startswith("ticket-"):
            await ctx.channel.delete()
        else:
            await ctx.send("This command can only be used in a ticket channel.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
