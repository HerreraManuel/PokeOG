import discord
from discord.ext import commands
import json
import asyncio
import random
import os
from database import db


bot = commands.Bot(command_prefix='!')

with open('config.json') as config:
    config_data = json.load(config)

token = os.environ('BOT_TOKEN')


# list of our cogs
cog_collection = ['cogs.encounter']

# load the cogs, print error if otherwise
if __name__ == '__main__':
    for single_cog in cog_collection:
        try:
            bot.load_extension(single_cog)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print("Bot is running...")
    # Bot Status 
    await bot.change_presence(activity=discord.Game("Pokémon Red"))

bot.run('token')

