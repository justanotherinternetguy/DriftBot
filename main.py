import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents().all()
intents.members = True
description = "DriftBot: MADE BY justanotherinternetguy#9404"
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='~', intents=intents)

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print("cogs loading")
    for f in os.listdir("./cogs"):
        try:
            if f.endswith(".py"):
                await bot.load_extension(f"cogs.{f[:-3]}")
                print(f + " loaded")
        except Exception as e:
            print(e)

bot.run(DISCORD_TOKEN)
