from game import location
import game.config as config
from game.display import announce
from game.events import *
import game.items as items
import game.locations.adamB_utils.town_locs as shops
import game.locations.adamB_utils.adams_items as ab_items
import random
from game.events.adamB_events import *

class Flags:
    knowledge_flag = False
    map_flag = False
    supply_flag = False
    quest_flag = False

class Settled_Island(location.Location):
    def __init__(self,x,y,w):
        super().__init__(x,y,w)
        self.name = "Settled Island"
        self.symbol = "\u0413"
        self.visitable = True
        self.starting_location = Docks(self) #Insert Starting Location Here
        self.locations = {}
        self.locations["docks"] = self.starting_location
        self.locations["wharf"] = Wharf(self)
        self.locations["beach"] = Beach(self) 
        self.locations["jungle"] = Jungle(self) 
        self.locations["lumber camp"] = Lumber_camp(self) 
        #might make a seperate import for these locations
        self.locations["town"] = Town(self)
        self.locations["tavern"] = shops.Tavern(self)
        self.locations["casino"] = shops.Casino(self) 
        self.locations["store"] = shops.Store(self) 

    def enter(self,ship):
        print("You Arrive at the settled island")

    def visit(self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Docks (location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name="docks"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['south'] = self
        self.event_chance = 0

    def enter(self):
        announce("You step upon the docks")
    
    def process_verb (self,verb,cmd_list, nouns):
        if verb == "south":
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif verb == "north":
            config.the_player.next_loc = self.main_location.locations["wharf"]
        elif (verb == "east") or (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["beach"]

class Wharf (location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "wharf"
        self.verbs['north'] = self
        self.verbs['south'] = self
        #no east or west
        self.verbs['talk'] = self
        self.verbs['repair'] = self
        
    def enter(self):
        announce("You walk to the small wharf \n On the wharf is a stranded merchant and a shipwright")
    
    def process_verb (self,verb,cmd_list,nouns):
        if verb == "south":
            config.the_player.next_loc = self.main_location.locations["docks"]
        elif verb == "north":
            config.the_player.next_loc = self.main_location.locations["town"]
        elif verb == "talk":
            if len(cmd_list) == 1:
                announce("You try to talk to nobody?")
            elif cmd_list[1] == "merchant":
                announce("You try to talk to the merchant")
            elif cmd_list[1] == "shipwright":
                announce("You try to talk to the shipwright")
            else:
                announce("That person isn't here")
        elif verb == "repair":
            announce("You ask the shipwright to fix your ship")
            if not Flags.quest_flag:
                announce("Shipwright: I don't have the supplies to fix your ship")
            else:
                pass #not implemented yet

class Town(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.verbs['south'] = self
        self.verbs['casino'] = self
        self.verbs['store'] = self
        self.verbs['tavern'] = self
        #non-go verbs
        self.verbs['talk'] = self
        #need to add more stuff here
    def enter(self):
        announce("You step into town concisting of cobbled roads and small buildings")
        #check flags from town
        Flags.knowledge_flag = True if self.main_location.locations['casino'].flag else False
        Flags.supply_flag = True if self.check_flags(config.the_player.inventory)[0] else False
        Flags.map_flag = True if self.check_flags(config.the_player.inventory)[1] else False

        print(f'Supply Flag:  {Flags.supply_flag}')     #debug code
        print(f'Knowledge Flag: {Flags.knowledge_flag}')#debug code
        print(f'Map Flag: {Flags.map_flag}') #debug code

    def check_flags(self,inv):
        return_list = [False,False]
        for item in inv:
            if isinstance(item,ab_items.equipment):
                return_list[0] = True
            if isinstance(item,ab_items.map):
                return_list[1] = True
        return return_list


    def process_verb(self, verb, cmd_list, nouns):
        print(verb)
        if verb =='south':
            config.the_player.next_loc = self.main_location.locations['wharf']
        elif verb == 'casino':
            config.the_player.next_loc = self.main_location.locations['casino']
        elif verb == 'store':
            config.the_player.next_loc = self.main_location.locations['store']
        elif verb == 'tavern':
            config.the_player.next_loc = self.main_location.locations['tavern']
        elif verb == "talk":
            announce("There is nobody arround")

class Beach(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        #navigation verbs
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['north'] = self
        #foraging verbs
        self.verbs['fish'] = self
        self.verbs['forage'] = self

    def enter(self):
        announce("You step foot upon a beach, to your north is a jungle")

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "east" or verb =="west":
            config.the_player.next_loc = self.main_location.locations['docks']
        elif verb == "north":
            config.the_player.next_loc = self.main_location.locations['jungle']
        elif verb == "fish":
            pass
            #this code is for fishing, might be a minigame idk
        elif verb =="forage":
            pass
            #this code is for foraging the beach, source of income, but finite resources available.
        

class Jungle(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['shortcut'] = self
        self.verbs['forage'] = self
        self.event_chance = 100
        self.events.append(jungle_fruit.Fruit())
        self.events.append(animal_encounter.Tiger_fight())
    def enter(self):
        announce("You step foot into a dense jungle, any trace of human activity has been wiped away")

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "shortcut":
            config.the_player.next_loc = self.main_location.locations['lumber camp']#debug code
        if verb == "north":
            if Flags.knowledge_flag and Flags.map_flag and Flags.supply_flag:
                config.the_player.next_loc = self.main_location.locations['lumber camp']
            elif Flags.knowledge_flag and Flags.map_flag:
                announce("You follow the designated trails but the foliage proves to be too challenging, you are forced to turn back before reaching your destination.")
                event_dice = random.randint(1,10)
                #implement some events to happen when failing to navigate jungle
            elif Flags.knowledge_flag and Flags.supply_flag:
                announce("You cut through the folliage in search of the lumber camp but the jungle proves too difficult to navigate and you wander in a big circle.")
                event_dice = random.randint(1,10)
                #implement some events to happen when failing to find camp
            else:
                announce("Your lack of tools and knowledge make it impossible to find the lumber camp.")
                event_dice = random.randint(1,10)
                #implement some events to happen when failing to find camp
        elif verb == "south":
            config.the_player.next_loc = self.main_location.locations['beach']
        elif verb == "forage":
            pass
class Lumber_camp(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.verbs['south'] = self
        self.event_chance = 100
        self.events.append(boss_fight.Boss_Fight())

    def enter(self):
        if not isinstance(self.events[0],boss_fight.Boss_Fight):
            self.event_chance = 0
            Flags.quest_flag = True
            print("You have completed the quest") #debug code
        
        if Flags.quest_flag == False:
            announce("You make your way through the thck folliage into where the logging camp once was, to your suprise you find moving, sentient plants.\n They turn to face you and strike")
        elif Flags.quest_flag == True:
            announce("You enter the damaged logging camp, it will take some time before it's operational again.")

    def check_completion(self):
        if not isinstance(self.events[0], boss_fight.Boss_Fight):
            Flags.quest_flag = True
            print("quest flag set") #debug code
    def process_verb(self, verb, cmd_list, nouns):
        if verb == "south":
            config.the_player.next_loc = self.main_location.locations['jungle']
