import game.items as items

class equipment(items.Item):
    def __init__(self):
        super().__init__('Jungle Equipment',150)

class map(items.Item):
    def __init__(self):
        super().__init__('Tattered Map',0)

class Jungle_fruits(items.Item):
    def __init__(self):
        super().__init__("Jungle Fruits",20)
        #these are meant to be sold to the storekeep in order to purchase proper jungle equipment