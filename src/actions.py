import discord
from discord.ext import commands
from discord.ext.commands.view import quoted_word
import logging
import inspect

import votes

bot = commands.Bot(command_prefix='?', description="")

pokes = []

@bot.command(pass_context=True)
async def vote(ctx):
    number = [
            '🥔',
            '🥓',
            '👽',
            '🙃',
            '\N{Digit Five}',
            '\N{Digit Six}',
            '\N{Digit Seven}',
            ]
    view = ctx.view
    args = []
    while not view.eof:
        view.skip_ws()
        args.append(quoted_word(view))

    msg = votes.vote(*args)

    response = await bot.say(msg)

    for mention in response.mentions:
        pokes.append({
            'user_id': mention.id,
            'channel_name': response.channel,
            'message_id': response.id
            })
    
    if response.server is not None:
        for mention in response.role_mentions:
            for member in response.server.members:
                for role in member.roles:
                    if role == mention:
                        pokes.append({
                            'user_id': member.id,
                            'channel_name': response.channel,
                            'message_id': response.id
                            })
                        logging.info(pokes)

    for i in range(0,len(args)-1):
        await bot.add_reaction(response,number[i])

@bot.event
async def on_reaction_add(reaction,user):
    for i, poke in enumerate(pokes):
        if user.id == poke['user_id']:
            if reaction.message.id == poke['message_id']:
                del pokes[i]
                break

@bot.event
async def on_member_update(before,after):
    if before.status != after.status and before.status == discord.Status.offline:
        for poke in pokes:
            if after.id == poke['user_id']:
                await bot.send_message(
                        after,
                        f"You have a vote going on in #{poke['channel_name']}, get on it!")
