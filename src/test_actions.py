import unittest
import actions
import asyncio

message = ""
async def mockSay(something):
    global message
    message = something

actions.bot.say = mockSay

class TestActionVote(unittest.TestCase):

    def test_StartVote(self):
        """Should send the poll message when started"""

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        async def run_test():
            options = [("dude","what","something","two"),
                    ("potatoes","funny","chirstmas eve", "woah!"),
                    ("yes indeed", "not really", "ASD FQWE FAW DSF", "©")]
            for opt in options:
                await actions.vote.callback("start", *opt)
                self.assertEqual(message, (f"{opt[0]}\n"
                    f":one: {opt[1]}\n"
                    f":two: {opt[2]}\n"
                    f":three: {opt[3]}"))

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
