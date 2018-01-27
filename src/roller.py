from bs4 import BeautifulSoup
import urllib.request
from table import Table
import random

# Very simple performance improvement:
# Load the index just once on startup and reuse
IndexPage = urllib.request.urlopen("https://www.reddit.com/r/BehindTheTables/wiki/index")

class Roller:
    def __init__(self, table, html=None):
        if html is None:
            html = IndexPage
        soup = BeautifulSoup(html, "html.parser")
        self.table_link = None
        for link in soup.find_all('a'):
            if link.get_text().lower() == table.lower():
                self.table_link = link

    def load_table(self, html = None):
        if html is None:
            html = urllib.request.urlopen(self.table_link.get('href'))

        self.table_soup = BeautifulSoup(html, "html.parser")
        self.table = []

        for maybe_table in self.table_soup.find_all('strong'):
            if maybe_table.get_text().startswith('d'):
                split = maybe_table.get_text().split()
                t = Table(" ".join(split[1:]))
                t.set_die(split[0])

                #Get the lis from the next element (an ol)
                for item in maybe_table.find_next().findChildren():
                    t.add_item(item.get_text())
                self.table.append(t)

    def get_table_link(self):
        return self.table_link.get('href')

    def roll_it(self):
        result = []
        for t in self.table:
            items = t.items.copy()
            result.append({'title': t.title, 'choice': random.choice(items)})
        return result
