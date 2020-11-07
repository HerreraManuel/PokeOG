import discord
from discord.ext import commands

class Encounter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Clog.encounter()
    async def wild(ctx):
        # Generate random value between 1 - 151 
        random_poke = random.randint(1, 152)
        poke_Info = await db.wild_encounter(random_poke)
        current_pokemon = poke_Info["name"]
        embed=discord.Embed(description="Guess the pokémon and type !catch <pokémon> \nto catch it!", color=0x18b48d)
        # embed.set_author(name="A wild {} has appeared!".format(poke_Info["name"]))
        embed.set_author(name="A wild pokémon has appeared!")
        img_loc = "res/img/{}.png".format(poke_Info["name"])
        file=discord.File(img_loc, filename="poke.png")
        embed.set_image(url="attachment://poke.png")
        embed.set_footer(text="Type !help to see a list of commands")
        await ctx.send(file=file, embed=embed)

def setup(bot):
    bots.add_cog(Encounter(bot))
