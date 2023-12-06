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

    def display(self):
        print("You can sell: ")
        iterator = 1 
        for i in config.the_player.inventory:
            print(f'{iterator}: {i} for {i.getValue()} shillings')
            iterator += 1
    
    def sell_item(self,item):
        if isinstance(item,int):
            if item > 0 and item <= len(config.the_player.inventory):
                confirm = input(f'Are you sure you want to sell {config.the_player.inventory[item-1]}? Type yes to confirm: ')
                if confirm == 'yes' or confirm == 'Yes' or confirm == 'y' and not isinstance(config.the_player.inventory[item-1],a_items.map):
                    config.the_player.shillings += config.the_player.inventory[item-1].getValue()
                    config.the_player.inventory.pop(item-1)
            else:
                announce("Shopkeep: Can't sell something you don't have")
        else:
            announce("Please use the item number from the list above.")
    
    def sell_sequence(self):
        self.display()
        try:
            item = int(input("Which number item would you like to sell: "))
        except:
            announce("Please use a number from the list.")
        else:
            self.sell_item(item)

