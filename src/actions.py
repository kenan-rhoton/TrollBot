import discord
from discord.ext import commands

import votes

bot = commands.Bot(command_prefix='?', description="")

@bot.command()
async def vote(*choices : str):
    msg = votes.vote(*choices)
    await bot.say(msg)
