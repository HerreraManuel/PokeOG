import discord
from discord.ext import commands
import json
import asyncio
import random
from database import db

bot = commands.Bot(command_prefix='!')
current_pokemon = ""
with open('config.json') as config:
    config_data = json.load(config)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print("Bot is running...")
    # Bot Status 
    await bot.change_presence(activity=discord.Game("Pokémon Red"))

@bot.command()
async def wild(ctx):
    # Generate random value between 1 - 151 
    random_poke = random.randint(1, 152)
    poke_Info = await db.wild_encounter(random_poke)
    current_pokemon = poke_Info["name"]
    embed=discord.Embed(description="Guess the pokémon and type !catch <pokémon> \nto catch it!", color=0x18b48d)
    embed.set_author(name="A wild {} has appeared!".format(poke_Info["name"]))
    img_loc = "res/img/{}.png".format(poke_Info["name"])
    file=discord.File(img_loc, filename="poke.png")
    embed.set_image(url="attachment://poke.png")
    embed.set_footer(text="Type !help to see a list of commands")
    await ctx.send(file=file, embed=embed)

# catch command to check if user successfully caught a pokemon
@bot.command()
async def catch(ctx):
    await ctx.send("Congratulations USER! You caught a POKEMON! Added to Pokédex.")


bot.run(config_data['token'])
