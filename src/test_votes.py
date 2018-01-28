import unittest
import votes

class TestVote(unittest.TestCase):

    def test_Vote(self):
        """Should return a message when called with enough arguments"""

        options = [("dude","what","something","two"),
                ("potatoes","funny","chirstmas eve", "woah!"),
                ("yes indeed", "not really", "ASD FQWE FAW DSF", "©")]
        for opt in options:
            message, error = votes.vote(*opt)
            self.assertIsNone(error)
            self.assertEqual(message, (f"{opt[0]}\n"
                f":regional_indicator_a: {opt[1]}\n"
                f":regional_indicator_b: {opt[2]}\n"
                f":regional_indicator_c: {opt[3]}"))

    def test_VoteFewArgs(self):
        """Should return a usage message without enough args"""

        msg = "Usage: ?vote \"Vote title\" \"Option 1\" \"Option 2\" \"...\""
        message, error = votes.vote("one")
        self.assertEqual(error,"NotEnoughArgs")
        self.assertEqual(msg, message)
