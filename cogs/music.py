# cogs/music.py

import discord
from discord.ext import commands
import youtube_dl

ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0"  # bind to ipv4 since ipv6 might cause issues
}

ffmpeg_options = {
    "options": "-vn"
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or discord.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if "entries" in data:
            data = data["entries"][0]
        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join_voice(self, ctx):
        """Join the user's voice channel."""
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
            await ctx.send("Joined voice channel.")
        else:
            await ctx.send("You need to be in a voice channel first.")

    @commands.command(name="leave")
    async def leave_voice(self, ctx):
        """Leave the current voice channel."""
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Left the voice channel.")
        else:
            await ctx.send("I'm not in a voice channel.")

    @commands.command(name="play")
    async def play_song(self, ctx, *, url):
        """Play a song from a URL (YouTube, etc.)."""
        if not ctx.voice_client:
            await ctx.invoke(self.join_voice)

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f"Player error: {e}") if e else None)

        await ctx.send(f"Now playing: {player.data['title']}")

    @commands.command(name="pause")
    async def pause_song(self, ctx):
        """Pause the currently playing song."""
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("Playback paused.")
        else:
            await ctx.send("No audio is playing.")

    @commands.command(name="resume")
    async def resume_song(self, ctx):
        """Resume a paused song."""
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("Playback resumed.")
        else:
            await ctx.send("No audio is paused.")

    @commands.command(name="stop")
    async def stop_song(self, ctx):
        """Stop the currently playing song."""
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("Playback stopped.")
        else:
            await ctx.send("No audio is playing.")

async def setup(bot):
    await bot.add_cog(Music(bot))
