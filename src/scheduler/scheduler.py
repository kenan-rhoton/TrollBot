import parsedatetime
import datetime
from .schedule_data import _weekdays, _months

import logging

def FormatDate(date):
    wday = _weekdays[date.weekday()]
    month = _months[date.month-1]
    return f"{wday} {date.day} de {month} a les {date.hour}:{date.minute:02}"


class Scheduler:
    def __init__(self):
        self.cal = parsedatetime.Calendar(version=parsedatetime.VERSION_CONTEXT_STYLE)
        self.events = [] # Array of datetimes

    def add(self, **kwargs):
        time = kwargs.get('time',None)
        now = kwargs.get('now',None)
        if time is not None:
            res = self.cal.nlp(time, now)
            if res is not None:
                self.events.append(res[0][0])

    def getEvents(self):
        res = []
        for event in self.events:
            res.append(FormatDate(event))
        return res


    def purge(self,now=None):
        if now is None:
            now = datetime.datetime.now()
        else:
            now = datetime.datetime(*now[:6])
        for event in self.events.copy():
            if event < now:
                self.events.remove(event)

    def remove(self, item):
        del self.events[item]

    def process(self, args_list, now=None):

        self.purge(now=now)

        if len(args_list) > 0 and args_list[0] == "list":
            events = self.getEvents()

            for i, event in enumerate(events):
                events[i] = str(i+1) + ": " + event

            return "\n".join(events)

        elif len(args_list)>1 and args_list[0] == "delete":
            try:
                num = int(args_list[1])
                self.remove(num-1)
                return "Eliminat amb èxit"
            except:
                return "No existeix l'event \"" + args_list[1] + "\""

        else:
            self.add(time=" ".join(args_list), now=now)
            return "Afegit: " + self.getEvents()[-1]
