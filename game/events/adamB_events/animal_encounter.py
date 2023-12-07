import game.event as event
import random
import game.combat as combat
import game.superclasses as superclasses
from game.display import announce

class Tiger_fight (event.Event):
    def __init__ (self):
        self.name = " animal encounter"

    def process (self, world):
        result = {}
        result["message"] = "You survive the encounter."
        monsters = []
        min = 1
        uplim = 2
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing:
            monsters.append(Tiger("Tiger "+str(n)))
            n += 1
        announce (f"While exploring the jungle you are attacked by {'a' if n_appearing == 1 else 'two'} tiger{'s' if n_appearing == 2 else ''}")
        combat.Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result


class Tiger(combat.Monster):
    def __init__ (self, name):
        attacks = {}
        #attacks['name'] = ['verb','accuracy range','damage range']
        attacks["claw"] = ["claws",random.randrange(50,60), (5,10)]
        attacks["bite"] = ["bites",random.randrange(20,40), (10,15)]
        #7 to 19 hp, bite attack, 65 to 85 speed (100 is "normal")
        super().__init__(name, random.randrange(25,50), attacks, 75 + random.randrange(-10,35))