import discord
from discord.utils import get
from discord.ext import commands
import random
from datetime import timedelta
import json
import requests

class Auton(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Auton.cog READY")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = discord.utils.get(member.guild.channels, id=735157757308829801)

        embed = discord.Embed(title="Welcome **{0.name}!**".format(member), description=":tada:", color=0x5350b3)
        # embed.set_thumbnail(url="{0.avatar}".format(member))
        embed.add_field(name="Id:", value="{0.id}".format(member), inline=False)
        embed.add_field(name="Join Date:", value="{0.joined_at}".format(member), inline=False)
        embed.add_field(name="Mention:", value="{0.mention}".format(member), inline=False)
        
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = discord.utils.get(member.guild.channels, id=735157757308829801)

        embed = discord.Embed(title="Goodbye **{0.name}!**".format(member), description=":cry:", color=0xff0000)
        
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 581184089898352640:
            await message.add_reaction("🤓");
        
        if message.author.id == 1002315103909191701:
            await message.add_reaction("💩");

        
async def setup(bot):
    await bot.add_cog(Auton(bot))
