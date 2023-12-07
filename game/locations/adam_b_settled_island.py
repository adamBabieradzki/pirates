from game import location
import game.config as config
from game.display import announce
from game.events import *
import game.items as items
import game.locations.adamB_utils.town_locs as shops
import game.locations.adamB_utils.adams_items as ab_items
import random
from game.events.adamB_events import *
import game.locations.adamB_utils.forage as forage

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
        self.first_time = True

    def enter(self):
        announce("You step upon the docks")
        if self.first_time:
            self.first_time = False
            announce("If you need help with commands or progression you can find a guide in game/locations/adamB_utils/guide.txt, good luck and have fun !",pause=False)
    
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
                if not Flags.quest_flag:
                    announce("Merchant: My ship broke down with goods on board but I can't repair it here because of the lack of lumber")
                else:
                    announce("Merchant: I heard from the shipwright that I'll be out of here in a few weeks!")
            elif cmd_list[1] == "shipwright":
                if not Flags.quest_flag:
                    announce("Shipwright: I havn't been able to repair anything since the lumber camp was run over")
                else:
                    announce("Shipwright: I heard you cleared out the camp, thank you so much!")
            else:
                announce("That person isn't here")
        elif verb == "repair":
            announce("You ask the shipwright to fix your ship")
            if not Flags.quest_flag:
                announce("Shipwright: I don't have the supplies to fix your ship.")
            else:
                announce("Shipwright: Your ship doesn't look damaged.")

class Town(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.verbs['south'] = self
        self.verbs['casino'] = self
        self.verbs['store'] = self
        self.verbs['tavern'] = self
        #non-go verbs
    def enter(self):
        announce("You step into town concisting of cobbled roads and small buildings\n the buildings include a store, tavern, and casino")
        #check flags from town
        Flags.knowledge_flag = True if self.main_location.locations['casino'].flag else False
        Flags.supply_flag = True if self.check_flags(config.the_player.inventory)[0] else False
        Flags.map_flag = True if self.check_flags(config.the_player.inventory)[1] else False

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
        self.foraging = forage.BeachForage()
        self.fishing = forage.BeachFishing()

    def enter(self):
        announce("You step foot upon a beach, to your north is a jungle.\nThere should be some things on the beach worth foraging.\nIt looks like there are plentiful fish in the water")

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "east" or verb =="west":
            config.the_player.next_loc = self.main_location.locations['docks']
        elif verb == "north":
            config.the_player.next_loc = self.main_location.locations['jungle']
        elif verb == "fish":
            fishy = self.fishing.fish()
            if fishy != None:
                announce(f"You caught a {str(fishy)}")
                config.the_player.inventory.append(fishy)
            else:
                announce('You fail to catch the fish') 
        elif verb =="forage":
            item = self.foraging.forage()
            if item != None:
                announce(f"While foraging the beach you find a {str(item)}")
                config.the_player.inventory.append(item)
            else:
                announce("You foraged on the beach but could not find anything.")
        

class Jungle(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['forage'] = self
        self.event_chance = 60
        self.events.append(jungle_fruit.Fruit())
        self.events.append(animal_encounter.Tiger_fight())
        self.foraging = forage.JungleForage()

    def enter(self):
        announce("You step foot into a dense jungle, any paths north that were once clear are overgrown. Looks like there are a few things worth foraging in here as well.")

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "north":
            if Flags.knowledge_flag and Flags.map_flag and Flags.supply_flag:
                config.the_player.next_loc = self.main_location.locations['lumber camp']
            elif Flags.knowledge_flag and Flags.map_flag:
                announce("You follow the designated trails but the foliage proves to be too challenging, you are forced to turn back before reaching your destination.")
            elif Flags.knowledge_flag and Flags.supply_flag:
                announce("You cut through the folliage in search of the lumber camp but the jungle proves too difficult to navigate and you wander in a big circle.")
            else:
                announce("Your lack of tools and knowledge make it impossible to find the lumber camp.")
        elif verb == "south":
            config.the_player.next_loc = self.main_location.locations['beach']
        elif verb == "forage":
            item = self.foraging.forage()
            if item != None:
                announce(f"While foraging in the jungle you find a {str(item)}")
                config.the_player.inventory.append(item)
            else:
                announce("You foraged in the jungle but could not find anything.")

class Lumber_camp(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.verbs['south'] = self
        self.event_chance = 100
        self.events.append(boss_fight.Boss_Fight(self))

    def enter(self):
        if Flags.quest_flag == False:
            announce("You make your way through the thick folliage into where the logging camp once was, to your suprise you find moving, sentient plants.\n They turn to face you and strike")
        elif Flags.quest_flag == True:
            announce("You enter the damaged logging camp, it will take some time before it's operational again.")

    def mark_complete(self):
        Flags.quest_flag = True
        print("")
    def process_verb(self, verb, cmd_list, nouns):
        if verb == "south":
            config.the_player.next_loc = self.main_location.locations['jungle']
