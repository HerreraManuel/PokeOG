import discord
from discord.ext import commands
import json
import asyncio
import sqlite3
import random
from db import db

bot = commands.Bot(command_prefix='!')

with open('config.json') as config:
    config_data = json.load(config)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print("Bot is running...")
    # Bot Status 
    await bot.change_presence(activity=discord.Game("Pokemon Red"))

@bot.command()
async def wild(ctx):
    # Generate random value between 1 - 151 
    randomPoke = random.randint(1, 152)
    pokemon = await db.wild_encounter(randomPoke)
    await ctx.send(pokemon)

bot.run(config_data['token'])