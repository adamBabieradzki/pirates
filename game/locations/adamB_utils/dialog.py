from game.display import announce
import game.config as config
import game.locations.adamB_utils.adams_items as items
import random

class Casino:
    def __init__(self,other):
        self.first_time = True
        self.other = other

        self.small_talk_list = (
                "Ever since the merchants stopped showing up business has been slow",
                "Have you visited the tavern yet?",
                "You want to know more about the island? Maybe if you beat me a few times."
        )
        self.popable_list = list(self.small_talk_list)
    def talk(self):
        if self.first_time:
            announce("Dealer: Your pockets seem a little light here are some chips, on the house.")
            self.other.chips = 5
            self.first_time = False
        elif self.other.flag == True:
            announce("Dealer: I wish I could tell you where exactly the logging camp is, but I'm just the casino owner "+
                     "\nmaybe if you spoke with someone who worked there they would be able to tell you.")
        elif self.other.chips == 0 and config.the_player.shillings > 0:
            announce("Dealer: You can by some chips for 10 shillings per chip")
            decision = input("Buy chips? y/n")
            if decision == "y":
                decision2 = input("How Many?")
                try:
                    decision2_i = int(decision2)
                except:
                    announce(f"Dealer: I can't sell you {decision2} chips")
                else:
                    if decision2_i <= config.the_player.shillings * 10:
                        config.the_player.shillings += (-decision2_i * 10)
                        self.other.chips += decision2_i
                    else:
                        announce(f"Dealer: You don't have enough for {decision2} chips.") 
        else:
            announce("You try to make small talk with the dealer")
            if len(self.popable_list) > 0:
                announce(self.popable_list.pop(random.randint(0,len(self.popable_list)-1)))
            else:
                self.popable_list = list(self.small_talk_list)
                announce(self.popable_list.pop(random.randint(0,len(self.popable_list)-1)))

class Shop:
    def __init__(self,other):
        self.other = other
        self.first_time = True
        self.hint = True
    def talk(self):
        if self.first_time:
            self.first_time = False
            announce() #first time text
        elif config.the_player.shillings < 200 and self.hint:
            self.hint = False
            announce("Shopkeep: Your pockets seem a little light, I would suggest checking in the tavern if there's any work available.")
        else:
            announce("Shopkeep: I promise my inventory is usually better, but the lack of regular shipments have")


class Tavern:
    def __init__(self,other):
        self.other = other
        self.person1_first_time = True
        self.person2_first_time = True
    def talk(self,target=None):
        if target == None:
            announce("Barkeep: Welcome, can I get you anything to eat or perhaps a drink?\nThere only seems to be one other patron in the tavern")
        if target == "Barkeep":
            if self.person1_first_time:
                announce("Barkeep: It's been a while since someone arrived to this backwater island especially a pirate\nunfortunatly you won't find much loot around here")
                self.person1_first_time = False
            else:
                announce("Barkeep: The other person in here?, oh that's the old foreman for the inland camp, one of the few who made it out unharmed.")
        if target == "Foreman":
            if self.person2_first_time:
                announce("Foreman: I used to run the lumber mill further inland, the mill is overgrown and many of the workers are dead or have left the island\nI could't imagine why anyone would want to return to that god forsake place")
                self.person2_first_time = False
            else:
                announce("After some convincing the foreman agrees to tell you how to get to the camp\nForeman: If you incist on making your way to the camp then I won't stop you, but I will warn you that all who atempted it havn't returned."+
                         "\nOn a tattered piece of parchment the foreman scribbles a rough map of the island, which shows all of the paths leading to the mill.")
                
        