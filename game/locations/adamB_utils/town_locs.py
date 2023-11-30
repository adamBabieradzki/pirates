from game import location
import game.config as config
from game.display import announce
from game.events import *
import game.items as items
import game.locations.adamB_utils.mini_game as blackjack
import game.locations.adamB_utils.dialog as dialog

class Casino(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.talk = dialog.Casino(self)
        self.name = "casino"
        self.verbs['town'] = self
        self.verbs['talk'] = self
        self.verbs['gamble'] = self
        self.chips = 0
        self.wincount = 0
        self.flag = False

    def enter(self):
        announce("You walk into a casino that looks more like someone's parlor room. ")    

    def process_verb (self,verb,cmd_list, nouns):
        if verb == "town":
            config.the_player.next_loc = self.main_location.locations["town"]
        elif verb == 'talk':
            self.talk.talk()
        elif verb == 'gamble':
            game = blackjack.Game()
            announce(f'You have {self.chips} chips.')
            if self.chips > 0:
                while input("Dealer: Would you like me to deal you in? (y/n)") in ("y","Y","yes","Yes") and self.chips > 0:
                    if game.play_game() == "player": 
                        self.wincount += 1
                        self.chips += 1
                    else:
                        self.chips -= 1
                    print(self.wincount)
                    if self.wincount >= 5 and self.flag == False:
                        announce("Dealer: You've been winning a lot of games, how about I pay you in the form of an IOU to the clerk next door \n the owed me a favor from a while back")
                        self.flag = True
                        break
            else:
                announce("If you don't have any chips talk to the dealer!")
        

class Store(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "store"
        self.verbs['town'] = self
        self.verbs['buy'] = self
        self.verbs['sell'] = self
        self.verbs['talk'] = self
        self.flag = False

    def enter(self):
        announce("A friendly looking clerk greets you as you enter the general store. ")

    def process_verb (self,verb,cmd_list, nouns):
        if verb == "town":
            config.the_player.next_loc = self.main_location.locations["town"]
        elif verb == "buy":
            pass
        elif verb == "sell":
            pass
        elif verb == "talk":
            pass
        
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