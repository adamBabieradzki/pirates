from game.display import announce
import game.config as config
import game.locations.adamB_utils.adams_items as items

class Casino:
    def __init__(self):
        self.first_time = True
    
    def talk(self):
        if self.first_time:
            announce("Dealer: Your pockets seem a little light here are some chips, on the house.")
            config.the_player.add_to_inventory([items.Chip(5)])