import game.event as event
import random
import game.combat as combat
import game.superclasses as superclasses
from game.display import announce
import game.events.nothing as nothing


class Boss_Fight(event.Event):
    def __init__(self):
        self.name = "boss fight"
    
    def process(self,world):
        result = {}
        result['message'] = "After a greuling fight you have defeated the sentient plants and liberated the camp."
        monsters1 = [SentientPlantType1("Sentient Plant 1"),
                     SentientPlantType1("Sentient Plant 2"),
                     SentientPlantType2("Sentient Plant 3"),
                     SentientPlantType2("Sentient Plant 4")]
        monsters2 = [SentientPlantType1("Sentient Plant 1"),
                     SentientPlantType1("Sentient Plant 2"),
                     SentientPlantType1("Sentient Plant 3"),
                     TheSeed("Large Pulsating Seed")]
        combat.Combat(monsters1).combat()
        announce("After defeating the plants you notice a man sized pulsating bulb in the center of the logging camp.")
        combat.Combat(monsters2).combat()
        result['newevents'] = [ nothing.Nothing() ]
        return result



class SentientPlantType1(combat.Monster):
    def __init__(self,name):
        attacks = {}
        attacks["coil"] = ["coils around", random.randrange(20,30), (10,20)]
        attacks["whip"] = ["whips", random.randrange(40,65), (3,10)]

        super().__init__(name, random.randrange(30,50), attacks, 100 + random.randrange(-20,20))

class SentientPlantType2(combat.Monster):
    def __init__(self,name):
        attacks = {}
        attacks['thorn'] = ["fires a thorn at", random.randrange(60,80), (6,12)]
        attacks['spit'] = ['spits at', random.randrange(20,30), (10,20)]

        super().__init__(name, random.randrange(30,50), attacks, 100 + random.randrange(-25,15))

class TheSeed(combat.Monster):
    def __init__(self,name):
        attacks = {}
        attacks["pulsate"] = ["pulsates at", 100, 0]

        super().__init__(name, 150, attacks, 100) 