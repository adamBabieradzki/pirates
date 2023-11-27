from game import location
import game.config as config
from game.display import announce
from game.events import *
import game.items as items
import game.locations.adamB_utils.mini_game as blackjack

class Casino(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "casino"
        self.verbs['town'] = self
        self.verbs['talk'] = self
        self.verbs['gamble'] = self
        self.wincount = 0
        self.flag = False

    def enter(self):
        announce("You walk into a casino that looks more like someone's parlor room. ")    

    def process_verb (self,verb,cmd_list, nouns):
        if verb == "town":
            config.the_player.next_loc = self.main_location.locations["town"]
        elif verb == 'talk':
            pass
        elif verb == 'gamble':
            game = blackjack.Game()
            while input("Dealer: Would you like me to deal you in? (y/n)") in ("y","Y","yes","Yes"):
                self.wincount += game.play_game()
                print(self.wincount)
                if self.wincount >= 5 and self.flag == False:
                    announce("Dealer: You've been winning a lot of games, how about I pay you in the form of an IOU to the clerk next door \n the owed me a favor from a while back")
                    self.flag = True
                    break

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