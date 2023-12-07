import game.event as event
import random
import game.combat as combat
import game.superclasses as superclasses
from game.display import announce
import game.events.nothing as nothing
import game.config as config
import game.locations.adamB_utils.adams_items as items

class Boss_Fight(event.Event):
    def __init__(self,m):
        self.name = "boss fight"
        self.m = m
    
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
        self.m.mark_complete()
        config.the_player.inventory.append(items.Chest())
        config.the_player.shillings += 100
        announce("After clearing all the plants in the camp you come across a shack with a chest containing 100 shillings and various bullion \n with only the foreman and a few workers left around you figure nobody will miss that much.")
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
        attacks["pulsate"] = ["pulsates at", random.randrange(99,100), (0,5)]

        super().__init__(name, 150, attacks, 100) 