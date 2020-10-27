import discord
import json

client = discord.Client()

with open('config.json') as config:
    config_data = json.load(config)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(config_data.token)