import discord
from discord.ext import commands
from discord.ext.commands.view import quoted_word

import votes
import poke
from roller import Roller

bot = commands.Bot(command_prefix='?', description="")

def get_quoted(view):
    res = []
    while not view.eof:
        view.skip_ws()
        res.append(quoted_word(view))
    return res

@bot.command(pass_context=True,description="Organize a vote")
async def vote(ctx):
    # Reaction representations MUST be Unicode or die
    number = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬']
    args = get_quoted(ctx.view)

    msg, err = votes.vote(*args)
    response = await bot.say(msg)

    # DO NOT PARSE THE RESPONSE IF WE HAD AN ERROR!
    if err is not None:
        return

    poke.add_pokes(response)

    for i in range(0,len(args)-1):
        await bot.add_reaction(response,number[i])

@bot.command(description="Roll a table from r/BehindTheTables")
async def roll(*table_name : str):
    roll = Roller(" ".join(table_name))

    if roll.table_link is None:
        await bot.say("Can't find that in https://www.reddit.com/r/BehindTheTables/wiki/index")
        return

    roll.load_table()
    result = roll.roll_it()
    msg = ""
    for res in result:
        msg += f"{res['title']} {res['choice']} "
    await bot.say(msg)

@bot.event
async def on_reaction_add(reaction,user):
    # Bad idea to modify a list you're iterating, so we iterate a copy
    for poke in poke.pokes.copy():
        if user.id == poke['user_id']:
            if reaction.message.id == poke['message_id']:
                pokes.remove_poke(poke)
                break

@bot.event
async def on_member_update(before,after):
    if before.status != after.status and before.status == discord.Status.offline:
        for poke in poke.pokes:
            if after.id == poke['user_id']:
                await bot.send_message(
                        after,
                        f"You have a vote going on in #{poke['channel_name']}, get on it!")
