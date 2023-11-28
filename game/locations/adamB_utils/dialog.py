from game.display import announce
import game.config as config
import game.locations.adamB_utils.adams_items as items

class Casino:
    def __init__(self,other):
        self.first_time = True
        self.other = other
    def talk(self):
        if self.first_time:
            announce("Dealer: Your pockets seem a little light here are some chips, on the house.")
            self.other.chips = 5
            self.first_time = False
        else:
            announce("Would you like to buy some chips?")
            self.other.chips += 1
    