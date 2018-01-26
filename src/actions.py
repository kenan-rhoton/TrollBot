import discord
from discord.ext import commands
from discord.ext.commands.view import quoted_word

import votes
import poke

bot = commands.Bot(command_prefix='?', description="")

def get_quoted(view):
    res = []
    while not view.eof:
        view.skip_ws()
        res.append(quoted_word(view))
    return res

@bot.command(pass_context=True)
async def vote(ctx):
    number = ['🥔','🥓','👽','🙃','☀','🙈','🌵']
    args = get_quoted(ctx.view)

    msg = votes.vote(*args)

    response = await bot.say(msg)

    poke.add_poke(response)

    for i in range(0,len(args)-1):
        await bot.add_reaction(response,number[i])

@bot.event
async def on_reaction_add(reaction,user):
    for i, poke in enumerate(poke.pokes):
        if user.id == poke['user_id']:
            if reaction.message.id == poke['message_id']:
                pokes.remove_poke(i)
                break

@bot.event
async def on_member_update(before,after):
    if before.status != after.status and before.status == discord.Status.offline:
        for poke in poke.pokes:
            if after.id == poke['user_id']:
                await bot.send_message(
                        after,
                        f"You have a vote going on in #{poke['channel_name']}, get on it!")
