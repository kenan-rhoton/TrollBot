import discord

#Activate logging
import logging
logging.basicConfig(level=logging.INFO)

#Import the actions module
import actions

#Import the config module
import config

conf = config.source('config.yml')

#Start the stuff
actions.bot.run(conf['discord_token'])
