import discord
import json
import asyncio

bot = discord.Client()

with open('config.json') as config:
    config_data = json.load(config)

@bot.event
async def on_ready():
    #print('We have logged in as {0.user}'.format(bot))
    print("Bot is running...")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot.run(config_data['token'])