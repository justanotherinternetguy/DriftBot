import discord
from discord.utils import get
from discord.ext import commands
import random
from datetime import timedelta
import json
import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

def get_ym_joke():
    resp = requests.get("https://api.yomomma.info/")
    data = json.loads(resp.text)
    return data

def get_cat_image():
    resp = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = json.loads(resp.text)
    quote = json_data[0]["url"]
    return quote

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun.cog READY")
        
    @commands.command(aliases=['CAT'])
    async def cat(self, ctx):
        img = get_cat_image()
        
        embed = discord.Embed(title="**CAT IMAGE**", color=0x000000)
        embed.set_image(url=img)
        await ctx.reply(embed=embed)

    @commands.command()
    async def catgirl(self, ctx):
        embed = discord.Embed(title="**bonk go to horny jail**", color=0x000000)
        embed.set_image(url="https://i.kym-cdn.com/entries/icons/original/000/033/758/Screen_Shot_2020-04-28_at_12.21.48_PM.png")
        await ctx.reply(embed=embed)

    @commands.command(aliases=["IQ"])
    async def intelligence(self, ctx, member: discord.Member=None):
        iq = str(random.randint(4, 170))
        if member is None: await ctx.reply("You have an IQ of: " + iq)
        else: await ctx.reply("Member {0.name} has an IQ of: ".format(member) + iq)

    @commands.command(aliases=['INSP'])
    async def inspire(self, ctx):
        quote = get_quote()
        embed = discord.Embed(title="**{0}**".format(quote), color=0x0000ff)
        await ctx.reply(embed=embed)
        
    @commands.command(aliases=['YM'])
    async def yourmom(self, ctx):
        joke = get_ym_joke()
        embed = discord.Embed(title="*{0}*".format(joke['joke']), color=0xff3300)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))
