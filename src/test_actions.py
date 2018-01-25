
# THIS DISCORD SHIT IS UNTESTABLE ASDFASDFADSF

#import unittest
#import actions
#import asyncio
#import discord
#
#message = ""
#async def mockSay(something):
#    global message
#    message = something
#
#actions.bot.say = mockSay
#
#class mockMention:
#    def __init__(self):
#        self.id = 3
#
#class mockMessage:
#    def __init__(self, mentions = [], channel = "a"):
#        self.mentions = mentions
#        self.channel = channel
#        self.id = 5
#        self.server = None
#
#class mockContext:
#    def __init__(self, args, msg = mockMessage()):
#        self.args = args
#        self.message = msg
#
#def async_test(test):
#    event_loop = asyncio.new_event_loop()
#    asyncio.set_event_loop(event_loop)
#    coro = asyncio.coroutine(test)
#    event_loop.run_until_complete(coro())
#    event_loop.close()
#
#class TestActionVote(unittest.TestCase):

#    def test_Vote(self):
#        """Should send the poll message when called with enough arguments"""
#        async def run_test():
#            options = [("dude","what","something","two"),
#                    ("potatoes","funny","chirstmas eve", "woah!"),
#                    ("yes indeed", "not really", "ASD FQWE FAW DSF", "©")]
#            for opt in options:
#                await actions.vote.callback(mockContext(opt))
#                self.assertEqual(message, (f"{opt[0]}\n"
#                    f":one: {opt[1]}\n"
#                    f":two: {opt[2]}\n"
#                    f":three: {opt[3]}"))
#        async_test(run_test)

#    def test_StoresMentionsToPoke(self):
#        """Should schedule a poke when a role or user is mentioned"""
#        actions.pokes = []
#        async def run_test():
#            args = ["poking @everyone", "1", "2"]
#            msg = mockMessage(mentions=[mockMention(),mockMention()])
#            await actions.vote.callback(mockContext(args, msg))
#            self.assertTrue(len(actions.pokes) > 0)
#
#        async_test(run_test)
#
