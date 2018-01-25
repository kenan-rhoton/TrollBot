import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?', description="")

@bot.command()
async def vote(*choices : str):
    msg = ""
    if len(choices) < 3:
        msg = f"Usage: {bot.command_prefix}vote \"Vote title\" \"Option 1\" \"Option 2\" \"...\""
    else:
        msg = f"{choices[0]}"
        number = ["one","two","three","four","five","six","seven"]
        for i, choice in enumerate(choices[1:]):
            msg += f"\n:{number[i]}: {choice}"
    await bot.say(msg)
