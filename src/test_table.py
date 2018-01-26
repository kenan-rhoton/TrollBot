import unittest
from table import Table

class TestTable(unittest.TestCase):

    def test_TableHasTitle(self):
        """Should save the title"""
        t = Table("tital")
        self.assertEqual(t.title,"tital")

    def test_TableAddsItems(self):
        """Should add the items"""
        t = Table("tital")
        items = ["Yo!","Potato!","go fish","baddd"]
        for i in items:
            t.add_item(i)

        self.assertEqual(t.items,items)

    def test_TableItemsGetTrimmed(self):
        """Should add the items"""
        t = Table("tital")
        items = ["    Yo!","Potato!    ","  go fish    ","baddd"]
        realitems = ["Yo!","Potato!","go fish","baddd"]
        for i in items:
            t.add_item(i)

        self.assertEqual(t.items,realitems)
