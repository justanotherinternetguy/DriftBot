import discord
from discord.utils import get
from discord.ext import commands
import random
import sys
import psutil


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utils.cog READY")


    @commands.command()
    async def patchnotes(self, ctx):
        """Get information about a new version release of the bot"""
        text = """hi"""
        ver = "0.1.0"
        embed = discord.Embed(title="**Release {0}**".format(ver), description="{0}".format(text), color=0x00ff00)
        await ctx.reply(embed=embed)
    
    @commands.command()
    async def ping(self, ctx):
        """Check ping/latency of your connection to the bot"""
        embed = discord.Embed(title="Pong!", color=0x000000)
        embed.add_field(name="Latency: ", value=f'{round(self.bot.latency * 1000)} ms')
        await ctx.reply(embed=embed)

    @commands.command()
    async def info(self, ctx, member: discord.Member):
        """Get the join information of a user"""
        embed = discord.Embed(title="Information for **{0.name}**".format(member), color=0x5350b3, description=":eye:")
        embed.set_thumbnail(url="{0.avatar}".format(member))
        embed.add_field(name="Id:", value="{0.id}".format(member), inline=False)
        embed.add_field(name="Join Date:", value="{0.joined_at}".format(member), inline=False)
        embed.add_field(name="Permissions:", value="{0.guild_permissions}".format(member), inline=False)
        embed.add_field(name="Color:", value="{0.color}".format(member), inline=False)
        embed.add_field(name="Roles:", value="{0.roles}".format(member), inline=False)
        embed.add_field(name="Mention:", value="{0.mention}".format(member), inline=False)
        await ctx.reply(embed=embed)
    
    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(title="Avatar of **{0.name}**".format(member), color=0x5350b3, description=":tada:")
        embed.set_thumbnail(url="{0.avatar}".format(member))
        embed.add_field(name="Link to PFP:", value="{0.avatar}".format(member), inline=False)
        embed.set_image(url="{0.avatar}".format(member))
        await ctx.reply(embed=embed)

    @commands.command()
    async def drop(self, ctx):
        await ctx.reply("hendry probably went to sleep at this point, he coded this link for all of you <3. welcome to 2023.: https://bye2022.surge.sh/")

    @commands.command()
    async def rng(self, ctx, param=None):
        """Generate random number
        Format must be in <# of numbers to generate>//<Posssible range of each number>"""
        rolls, limit = map(int, param.split('//'))
        
        if param is None:
            embed = discord.Embed(title="Error!", color=0xff0000)
            embed.add_field(name="Incorrect Format!", value="Format must be in <# of numbers to generate>**//**<Posssible range of each number>")
            await ctx.reply(embed=embed)
            return
        
        if rolls <= 0 or limit <= 0:
            embed = discord.Embed(title="Error!", color=0xff0000)
            embed.add_field(name="Incorrect Format!", value="The numbers cannot be equal to or less than 0")
            await ctx.reply(embed=embed)
            return
        
        if rolls > 800 or limit > 800:
            embed = discord.Embed(title="Error!", color=0xff0000)
            embed.add_field(name="Incorrect Format!", value="The numbers must be less than 700, there is NO WAY you need more than that.")
            await ctx.reply(embed=embed)
            return
        
        try:
            embed = discord.Embed(title="Random number generator")
            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            embed.add_field(name="Output:", value=result)
            # await ctx.reply(embed=embed)
            await ctx.reply(embed=embed)


        except Exception as e:
            embed = discord.Embed(title="Error!", color=0xff0000)
            embed.add_field(name="Incorrect Format!", value="Format must be in <# of numbers to generate>**//**<Posssible range of each number> (VALUES CANNOT BE UNDER 1)")
            embed.add_field(name="Incorrect Format!", value=e)
            await ctx.reply(embed=embed)

    @commands.command()
    async def server(self, ctx):
        """Get statistics and information about the server computer"""
        cpu_usage = psutil.cpu_percent(interval=0.1, percpu=True)
        cores = psutil.cpu_count()
        freq = psutil.cpu_freq()
        load = psutil.getloadavg()
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        temps = psutil.sensors_temperatures()
        fans = psutil.sensors_fans()
        battery = psutil.sensors_battery()
        users = psutil.users()

        embed = discord.Embed(title="Information for server: **{0}** on **{1}**".format(users[0][0], users[0][1]), color=0x5350b3, description=":eye:")
        embed.add_field(name="CPU Usage:", value="{0}".format(cpu_usage), inline=False)
        embed.add_field(name="CPU Core Count:", value="{0}".format(cores), inline=False)
        embed.add_field(name="CPU Freq:", value="{0} MHz".format(freq[0]), inline=False)
        embed.add_field(name="CPU Load:", value="{0}".format(load), inline=False)
        embed.add_field(name="RAM Usage:", value="{0}".format(ram), inline=False)
        embed.add_field(name="HDD Usage:", value="{0}".format(disk[0]), inline=False)
        embed.add_field(name="System Temperatures:", value="{0}".format(temps), inline=False)
        embed.add_field(name="Fan Speeds:", value="{0}".format(fans), inline=False)
        embed.add_field(name="Battery:", value="{0}".format(battery), inline=False)
        await ctx.reply(embed=embed)



async def setup(bot):
    await bot.add_cog(Utils(bot))
