import game.items as items

class equipment(items.Item):
    def __init__(self):
        super().__init__('Jungle Equipment',150)

class map(items.Item):
    def __init__(self):
        super().__init__('Tattered Map',0)