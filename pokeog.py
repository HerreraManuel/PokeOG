import discord
from discord.ext import commands
import json
import asyncio
import sqlite3

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
    db = sqlite3.connect("pokedex.sqlite")
    cursor = db.cursor()
    cursor.execute("""SELECT id, identifier
    FROM pokemon
    WHERE id=4;""")
    result = cursor.fetchall()
    await ctx.send(str(result[0]))

bot.run(config_data['token'])