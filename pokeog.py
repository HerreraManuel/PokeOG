import discord
from discord.ext import commands
import json
import asyncio
import random
from database import db

bot = commands.Bot(command_prefix='!')
current_pokemon = ""

# list of our cogs
cog_collection = ['cogs.Encounter']

with open('config.json') as config:
    config_data = json.load(config)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print("Bot is running...")
    # Bot Status 
    await bot.change_presence(activity=discord.Game("Pokémon Red"))



# catch command to check if user successfully caught a pokemon
@bot.command()
async def catch(ctx):
    await ctx.send("Congratulations USER! You caught a POKEMON! Added to Pokédex.")

for single_cog in cog_collection
    bot.load_extension(single_cog)
    
bot.run(config_data['token'])
