import unittest
from .scheduler import Scheduler

class TestScheduler(unittest.TestCase):

    def test_add(self):
        testData = [
                {
                    'time': "Tomorrow at 13:00",
                    'origin': (2018,2,5,6,0,0,0,0,0),
                    'result': "Dimarts 6 de Febrer a les 13:00"
                },
                {
                    'time': "Friday at 21:00",
                    'origin': (2018,2,5,6,0,0,0,0,0),
                    'result': "Divendres 9 de Febrer a les 21:00"
                },
                {
                    'time': "In six weeks at 20:00",
                    'origin': (2018,2,5,6,0,0,0,0,0),
                    'result': "Dilluns 19 de Març a les 20:00"
                },
                {
                    'time': "Thursday at 11:00",
                    'origin': (2014,8,4,23,30,0,0,0,0),
                    'result': "Dijous 7 de Agost a les 11:00"
                },
            ]
        s = Scheduler()
        for data in testData:
            s.add(time=data['time'],now=data['origin'])
        
        events = s.getEvents()

        for data in testData:
            self.assertIn(data['result'], events)

    def test_purge(self):
        origin = (2018,2,5,6,0,0,0,0,0)
        testGood = [
                {
                    'time': "Tomorrow at 13:00",
                    'result': "Dimarts 6 de Febrer a les 13:00"
                },
                {
                    'time': "In six weeks at 20:00",
                    'result': "Dilluns 19 de Març a les 20:00"
                },
            ]
        testBad = [
                {
                    'time': "Last Friday at 12:00",
                    'result': "Divendres 2 de Febrer a les 12:00"
                },
                {
                    'time': "Yesterday at 21:00",
                    'result': "Diumenge 4 de Febrer a les 21:00"
                },
            ]
        s = Scheduler()
        for data in testBad + testGood:
            s.add(time=data['time'], now=origin)
        
        s.purge(now=origin)
        events = s.getEvents()

        for data in testGood:
            self.assertIn(data['result'], events)

        for data in testBad:
            self.assertNotIn(data['result'], events)

    def test_remove(self):
        origin = (2018,2,5,6,0,0,0,0,0)
        testData = [
                {
                    'time': "Tomorrow at 13:00",
                    'result': "Dimarts 6 de Febrer a les 13:00"
                },
                {
                    'time': "In six weeks at 20:00",
                    'result': "Dilluns 19 de Març a les 20:00"
                },
            ]
        s = Scheduler()
        for data in testData:
            s.add(time=data['time'], now=origin)
        s.remove(0)
        events = s.getEvents()
        self.assertIn(testData[1]['result'], events)
        self.assertNotIn(testData[0]['result'], events)

    def test_process(self):
        origin = (2018,2,5,6,0,0,0,0,0)
        s = Scheduler()
        testGood = [
                {
                    'time': "Tomorrow at 13:00",
                    'result': "Afegit: Dimarts 6 de Febrer a les 13:00"
                },
                {
                    'time': "In six weeks at 20:00",
                    'result': "Afegit: Dilluns 19 de Març a les 20:00"
                },
            ]
        testBad = [
                {
                    'time': "Last Friday at 12:00",
                    'result': "Afegit: Divendres 2 de Febrer a les 12:00"
                },
                {
                    'time': "Yesterday at 21:00",
                    'result': "Afegit: Diumenge 4 de Febrer a les 21:00"
                },
            ]

        for data in testGood+testBad:
            self.assertEqual(
                    s.process(data['time'].split(),now=origin),
                    data['result']
                )

        self.assertEqual(
                s.process(["list"], now=origin),
                "1: Dimarts 6 de Febrer a les 13:00\n"
                "2: Dilluns 19 de Març a les 20:00"
            )
        s.process(["delete","2"], now=origin)
        self.assertEqual(
                s.process(["list"], now=origin),
                "1: Dimarts 6 de Febrer a les 13:00"
            )
