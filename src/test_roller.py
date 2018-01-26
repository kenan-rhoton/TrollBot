import unittest
from roller import Roller

class TestRoller(unittest.TestCase):

    def test_RollerFindsInitialLink(self):
        """Should get the appropriate table link from the HTML"""

        fakeHTML = '<html><body><a href="Not NICE!">WRONG!</a><a href="nice!">Correct, yay!</a></body></html>'
        roll = Roller("Correct, yay!",fakeHTML)

        self.assertEqual(roll.get_table_link(),"nice!")

    def test_RollerLoadsTable(self):
        """Should generate the tables from the HTML"""

        fakeHTML = '<html><body><a href="Not NICE!">WRONG!</a><a href="nice!">Correct, yay!</a></body></html>'
        roll = Roller("Correct, yay!",fakeHTML)
        fakeTable = '<html><body><p><strong>d4 You are...</strong></p><ol><li> Strong</li><li> Potato</li><li> Weak</li><li> Funny</li></ol></body></html>'

        roll.load_table(fakeTable)

        self.assertEqual(len(roll.table),1)
        self.assertEqual(roll.table[0].title,"You are...")
        self.assertEqual(roll.table[0].items,["Strong","Potato","Weak","Funny"])

    def test_RollerRollsSensibly(self):
        """Should generate the rolls from the tables"""

        fakeHTML = '<html><body><a href="Not NICE!">WRONG!</a><a href="nice!">Correct, yay!</a></body></html>'
        roll = Roller("Correct, yay!",fakeHTML)
        fakeTable = '<html><body><p><strong>d4 You are...</strong></p><ol><li> Strong</li><li> Potato</li><li> Weak</li><li> Funny</li></ol></body></html>'

        roll.load_table(fakeTable)

        results = roll.roll_it()

        self.assertEqual(len(results),1)
        self.assertEqual(results[0]['title'], "You are...")
        self.assertTrue(results[0]['choice'] in ["Strong","Potato","Weak","Funny"])
        

    def test_RollerMultiRoll(self):
        """Should generate the rolls from the tables when they have multiples"""

        fakeHTML = ''
        roll = Roller("",fakeHTML)
        bornOptions = ["in an Orc village",
                "at a very smelly inn",
                "in the Imperial Capital",
                "in the Northlands",
                "dead",
                "a potato"]
        fakeTable = """<html><body>
        <p><strong>d4 You are...</strong></p>
        <ol><li> Strong</li><li> Potato</li><li> Weak</li><li> Funny</li></ol>
        <p><strong>d6 ... and you were born ...</strong></p>
        <ol>"""
        for b in bornOptions:
            fakeTable += f"<li> {b}</li>"
        fakeTable += "</body></html>"

        roll.load_table(fakeTable)

        results = roll.roll_it()

        self.assertEqual(len(results),2)
        self.assertEqual(results[0]['title'], "You are...")
        self.assertTrue(results[0]['choice'] in ["Strong","Potato","Weak","Funny"])
        self.assertEqual(results[1]['title'], "... and you were born ...")
        self.assertTrue(results[1]['choice'] in bornOptions)
