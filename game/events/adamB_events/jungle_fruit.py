import game.event as event
import random
from game.display import announce
import game.config as config
from game.player import Player
from game.context import Context
import game.locations.adamB_utils.adams_items as items
class Fruit(Context,event.Event):
    def __init__(self):
        self.name = "Template"
        self.nouns = {}
        self.verbs = {}
        self.verbs['eat'] = self
        self.verbs['take'] = self
        self.verbs['leave'] = self
        self.n = random.randint(1,5)
    
    def process_verb(self,verb,cmd_list,nouns):
        if verb == "eat":
            announce("Despite your best judgement you decide to eat the fruit.")
            rand_roll = random.randint(1,100)
            if rand_roll >= 80:
                announce("The fruit were delicious and refreshing, the party regains some health",pause=False)
                for i in config.the_player.get_pirates():
                    i.health += 10
                self.go = True
            elif rand_roll < 80 and rand_roll >= 20:
                announce("The fruit was very bitter, but nobody got sick after eating it",pause=False)
                self.go = True
            elif rand_roll < 20:
                announce("The fruit was poisonous and the crew didn't feel well after consuming it.",pause=False)
                for i in config.the_player.get_pirates():
                    i.inflict_damage(random.randint(4,8),"was killed by poisonous fruit")
                self.go = True
        elif verb == "take":
            announce("You decide to take the fruit in hopes of selling it to the locals")
            inventory_space = True
            for i in config.the_player.inventory:
                if isinstance(i,items.Jungle_fruits):
                    inventory_space = False
            if inventory_space:
                for i in range(self.n):
                    config.the_player.inventory.append(items.Jungle_fruits())
            else:
                announce("You can't carry any more fruit.")
            self.go = True
        elif verb == "leave":
            announce("The fruit may be poisonous, you opt to leave it where it lies.")
            self.go = True
    
    def process(self,world):
        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = ""

        while (self.go == False):
            print ("You find some fruits in the jungle: ")
            Player.get_interaction ([self])

        return self.result

    