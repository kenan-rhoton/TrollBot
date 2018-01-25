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
                f":one: {opt[1]}\n"
                f":two: {opt[2]}\n"
                f":three: {opt[3]}"))


    def test_VoteMentionsStored(self):
        """Should be able to tell if a user is mentioned in title"""
        pass


