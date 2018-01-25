import unittest
import votes

class TestVote(unittest.TestCase):

    def test_Vote(self):
        """Should return a message when called with enough arguments"""

        options = [("dude","what","something","two"),
                ("potatoes","funny","chirstmas eve", "woah!"),
                ("yes indeed", "not really", "ASD FQWE FAW DSF", "©")]
        for opt in options:
            message = votes.vote(*opt)
            self.assertEqual(message, (f"{opt[0]}\n"
                f":potato: {opt[1]}\n"
                f":bacon: {opt[2]}\n"
                f":alien: {opt[3]}"))

    def test_VoteFewArgs(self):
        """Should return a usage message without enough args"""

        msg = "Usage: ?vote \"Vote title\" \"Option 1\" \"Option 2\" \"...\""
        self.assertEqual(msg, votes.vote("one"))
