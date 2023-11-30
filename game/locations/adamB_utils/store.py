import game.locations.adamB_utils.town_locs as store
import game.locations.adamB_utils.adams_items as a_items
import game.items as items
import game.config as config
from game.display import announce

class Buy():
    def __init__(self):
        self.items = {}
        self.items['cutlass'] = items.Cutlass()
        self.items['flintlock'] = items.Flintlock()
        self.items['jungle equipment'] = a_items.equipment()

    def display(self):
        announce(f"Shopkeeper: What would you like to buy?")
        for i, j in self.items.items():
            print(f'{i}: Price {j.getValue()}')        

    def purchase(self,item):
        if item in self.items.keys():
            if config.the_player.shillings >= self.items[item].getValue():
                config.the_player.inventory.append(self.items[item])
                config.the_player.shillings += -self.items[item].getValue()
                announce("Shopkeep: Thank you for your patronage!")
            else: 
                announce(f"Shoopkeep: You don't have enough shillings for {item.capitalize()}")
        else:
            announce("Shopkeep: I don't sell that.")
    
    def buy_sequence(self):
        self.display()
        buying = input("Item: ")
        self.purchase(buying)
class Sell():
    def __init__(self):
        pass