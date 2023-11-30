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
