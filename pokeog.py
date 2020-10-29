import discord
from discord.ext import commands
import json
import asyncio

bot = commands.Bot(command_prefix='!')

with open('config.json') as config:
    config_data = json.load(config)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print("Bot is running...")


@bot.command()
async def wild(ctx):
    await ctx.send('accepted!')

bot.run(config_data['token'])