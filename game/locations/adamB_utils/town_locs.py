from game import location
import game.config as config
from game.display import announce
from game.events import *
import game.items as items
import game.locations.adamB_utils.mini_game as blackjack
import game.locations.adamB_utils.dialog as dialog
import game.locations.adamB_utils.store as barter
class Casino(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.talk = dialog.Casino(self)
        self.name = "casino"
        self.verbs['town'] = self
        self.verbs['talk'] = self
        self.verbs['gamble'] = self
        self.verbs['cashout'] = self
        self.chips = 0
        self.wincount = 0
        self.flag = False

    def enter(self):
        announce("You walk into a casino that looks more like someone's parlor room. \n You can gamble, cashout, or talk with the dealer")    

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
                    if self.wincount >= 5 and self.flag == False:
                        announce("After winning for the 5th time the dealer reveals that the reason there is nobody else at his casino."+
                                 "\nDealer: The truth is no merchants have been ariving at the island because we lost contact with out inland"+
                                 "\nlogging camp.\nYou learn about the existence of this camp but don't know it's whereabouts."
                                 )
                        
                        self.flag = True
                        break
            else:
                announce("If you don't have any chips talk to the dealer!")
        elif verb == "cashout":
            if self.chips > 0:
                announce("You sell your chips to the dealer for 10 shillings each")
                announce(f"You sold {self.chips} chips for {self.chips * 10} shillings",pause=False)
                config.the_player.shillings += (self.chips * 10)
                self.chips = 0
            else:
                announce("You don't have any chips to cashout with")
        

class Store(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.talk = dialog.Shop(self)
        self.name = "store"
        self.verbs['town'] = self
        self.verbs['buy'] = self
        self.buy_class = barter.Buy()
        self.sell_class = barter.Sell()
        self.verbs['sell'] = self
        self.verbs['talk'] = self
        self.flag = False

    def enter(self):
        announce("A friendly looking clerk greets you as you enter the general store. You can buy or sell your goods here.")

    def process_verb (self,verb,cmd_list, nouns):
        if verb == "town":
            config.the_player.next_loc = self.main_location.locations["town"]
        elif verb == "buy":
            self.buy_class.buy_sequence()
        elif verb == "sell":
            self.sell_class.sell_sequence()
        elif verb == "talk":
            self.talk.talk()
        
class Tavern(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.talk = dialog.Tavern(self)
        self.name = "store"
        self.verbs['town'] = self
        self.verbs['talk'] = self
 
    def enter(self):
        announce("You take a seat at a round table towards the front, the owner of the tavern approaches you from accross the room. ")

    def process_verb (self,verb,cmd_list, nouns):
        if verb == "town":
            config.the_player.next_loc = self.main_location.locations["town"]
            announce("You return to town.")
        if verb == "talk":
            if len(cmd_list) == 1: #talk generally
                self.talk.talk(None)
            if len(cmd_list) == 2:
                if cmd_list[1] in self.talk.people:
                    self.talk.talk(cmd_list[1])
                else:
                    announce("That person isn't here")
