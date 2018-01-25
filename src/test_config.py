import unittest
import tempfile
import config

class TestConfig(unittest.TestCase):

    testdata = b'''
    test: "korrekt!"
    potatoes:
        - first
        - second
    '''

    def test_source_works(self):
        testfile = tempfile.NamedTemporaryFile()
        testfile.write(self.testdata)
        testfile.seek(0)
        conf = config.source(testfile.name)
        self.assertEqual(conf['test'],"korrekt!")
        self.assertEqual(conf['potatoes'],["first","second"])
