import discord
from discord.utils import get
from discord.ext import commands
from datetime import timedelta


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.cog READY")

    @commands.command(aliases=['P'])
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, count: int):
        """Purge messages from a channel"""
        await ctx.channel.purge(limit=int(count))

    @commands.command(aliases=['K'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, reason=None):
        """Kicks a user from the guild"""
        try:
            if ctx.message.author.guild_permissions.kick_members:
                await ctx.guild.kick(member, reason=reason)
                embed = discord.Embed(title="**KICK moderation**", description="Kicked {0.name}".format(member), color=0xff0000)
                await ctx.reply(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="**INCORRECT PERMISSIONS**", description="Make sure that the @DriftBot Role is at the TOP of the role hierarchy and has ALL the permissions turned on.", color=0xff0000)
            await ctx.reply(embed=embed)

    @commands.command(aliases=['M'])
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, string, reason=None):
        """Mutes/timeouts a member in the guild
        <days>/<hours>/<minutes>/<seconds>
        """
        if ctx.message.author.guild_permissions.moderate_members:
            days, hours, minutes, seconds = map(int, string.split('/'))
            duration = timedelta(days = int(days), hours = int(hours), minutes = int(minutes), seconds = int(seconds))
            await member.timeout(duration, reason=reason)
            embed = discord.Embed(title="**MUTE moderation**", description="Muted {0.name} for {1} days, {2}, hours, {3} minutes, {4} seconds".format(member, days, hours, minutes, seconds), color=0xff0000)
            await ctx.reply(embed=embed)


    @commands.command(aliases=['uM'])
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member, reason=None):
        """Unmutes a member in the guild"""
        if ctx.message.author.guild_permissions.moderate_members:
            await member.edit(timed_out_until=None)
            embed = discord.Embed(title="**UMMUTE moderation**", description="Unmuted {0.name}".format(member), color=0x00ff00)
            await ctx.reply(embed=embed)

    @commands.command(aliases=['B'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, reason=None):
        """Bans a member from the guild"""
        # if ctx.message.author.guild_permissions.ban_members:
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(title="**BAN moderation**", description="Banned {0.name}".format(member), color=0xff0000)
            await ctx.reply(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="**MISSING PERMISSIONS**", description="Contact a moderator or admin to run this command!", color=0xffffff)
            await ctx.reply(embed=embed)


    # PROBLEMS
    @commands.command(aliases=['uB'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, member: discord.Member):
        """Unbans a user from the guild"""
        banned_users = ctx.guild.bans()
        member_name, member_discrim = str(member).split('#')

        await ctx.guild.unban(member)
        await ctx.send("Unbanned {0.mention}".format(member))
        return


async def setup(bot):
    await bot.add_cog(Moderation(bot))
