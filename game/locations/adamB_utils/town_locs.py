from game import location
import game.config as config
from game.display import announce
from game.events import *
import game.items as items

class Casino(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "casino"
        self.verbs['town'] = self
        self.verbs['talk'] = self
        self.verbs['gamble'] = self

    def enter(self):
        announce("You walk into a casino that looks more like someone's parlor room. ")    

    def process_verb (self,verb,cmd_list, nouns):
        if verb == "town":
            config.the_player.next_loc = self.main_location.locations["town"]
        elif verb == 'talk':
            pass
        elif verb == 'gamble':
            pass

class Store(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "store"
        self.verbs['town'] = self

    def enter(self):
        announce("A friendly looking clerk greets you as you enter the general store. ")

    def process_verb (self,verb,cmd_list, nouns):
        if verb == "town":
            config.the_player.next_loc = self.main_location.locations["town"]

class Tavern(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "store"
        self.verbs['town'] = self

    def enter(self):
        announce("You take a seat at a round table towards the front, the owner of the tavern approaches you from accross the room. ")

    def process_verb (self,verb,cmd_list, nouns):
        if verb == "town":
            config.the_player.next_loc = self.main_location.locations["town"]