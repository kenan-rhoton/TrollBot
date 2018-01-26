class Table:
    def __init__(self, title):
        self.title = title
        self.items = []

    def add_item(self,item):
        self.items.append(item.strip())

    def set_die(self,die):
        self.die = die
