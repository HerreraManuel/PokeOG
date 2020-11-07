import discord
from discord.ext import commands
import json
import asyncio
import sqlite3
import random
from database import db

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
    random_poke = random.randint(1, 152)
    poke_Info = await db.wild_encounter(random_poke)
    embed=discord.Embed(color=0x18b48d)
    embed.set_author(name="A wild pokémon has appeared!",
        description="||test||")
    #embed.set_thumbnail(url=)
    #embed.add_field(name=, value=t, inline=True)
    #embed.set_footer(text=)
    await ctx.send(embed=embed)

bot.run(config_data['token'])