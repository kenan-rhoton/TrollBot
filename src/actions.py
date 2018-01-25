import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?', description="")

@bot.command()
async def vote(*choices : str):
    if choices[0] == "start":
        msg = ""
        if len(choices) < 4:
            msg = f"Usage: {bot.command_prefix}vote start \"Vote title\" \"Option 1\" \"Option 2\" \"...\""
        else:
            msg = f"{choices[1]}"
            number = ["one","two","three","four","five","six","seven"]
            for i, choice in enumerate(choices[2:]):
                msg += f"\n:{number[i]}: {choice}"
        await bot.say(msg)
