from . import poke
import unittest

class MockMention:
    def __init__(self):
        self.id = 0

class MockMessage:
    def __init__(self, mentions=[], channel = "", id = 0, server = None):
        self.mentions = mentions
        self.channel = channel
        self.id = id
        self.server = server

class TestPokes(unittest.TestCase):

    def test_add_pokes(self):
        message = MockMessage()
        message.mentions = [MockMention()]
        poke.pokes = []
        poke.add_pokes(message)
        self.assertTrue(len(poke.pokes) > 0)
        self.assertEqual(poke.pokes[0]['user_id'],message.mentions[0].id)

    def test_remove_poke(self):
        message = MockMessage()
        message.mentions = [MockMention()]
        poke.pokes = []
        poke.add_pokes(message)
        poke.remove_poke(poke.pokes[0])
        self.assertEqual(len(poke.pokes), 0)
