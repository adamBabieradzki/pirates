import game.items as items
import random
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

class Shell(items.Item):
    def __init__(self):
        super().__init__("Pretty Shell",30)

class Pearl(items.Item):
    def __init__(self):
        super().__init__("Pearl",200)

class Driftwood(items.Item):
    def __init__(self):
        super().__init__("Driftwood",5)

class Clam(items.Item):
    def __init__(self):
        super().__init__("Clam",10)

class Crab(items.Item):
    def __init__(self):
        super().__init__("Crab",10)

class Coconut(items.Item):
    def __init__(self):
        super().__init__("Coconut",20)

#rare wood, herbs, cacao beans, cinnamon, axe
class Rare_wood(items.Item):
    def __init__(self):
        super().__init__("Rare wood",30)

class Herbs(items.Item):
    def __init__(self):
        super().__init__("Medicinal Herbs",48)

class Cacao_beans(items.Item):
    def __init__(self):
        super().__init__("Cacao Beans",35)

class Cinnamon(items.Item):
    def __init__(self):
        super().__init__("Cinnamon",30)

class Axe(items.Item):
    def __init__(self):
        super().__init__("Lumber Axe",100)
        self.damage = (10,40)
        self.skill = "melee"
        self.verb = "strike"
        self.verb2 = "strikes"

class Fish(items.Item):
    def __init__(self):
        super().__init__("Fish", random.randint(5,50))

class Chest(items.Item):
    def __init__(self):
        super().__init__("Small chest with gold coins", 700)