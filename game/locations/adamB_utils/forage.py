import game.locations.adamB_utils.adams_items as pool_items
import random
import time

class BeachForage():
    def __init__(self):
        self.success_chance = 100
        self.atempts = 0
        self.item_pool = {
            "shell": pool_items.Shell(),
            "pearl": pool_items.Pearl(),
            "driftwood": pool_items.Driftwood(),
            "clam": pool_items.Clam(),
            "crab": pool_items.Crab(),
            "coconut": pool_items.Coconut()
        }
    
    def forage(self):
        if random.randint(0,100) < self.success_chance:
            roll = random.randint(1,100)
            self.atempts += 1
            self.success_chance = 100 * ((1 - .06) ** self.atempts)
            if roll >= 95:
                return self.item_pool["pearl"]
            else:
                key_list = list(self.item_pool.keys())
                key_list.remove("pearl")
                return self.item_pool[random.choice(key_list)]  
        else:
            return None

class JungleForage():
    def __init__(self):
        self.success_chance = 100
        self.atempts = 0
        self.axes = 2
        self.item_pool = {
            #rare wood, herbs, cacao beans, cinnamon, axe
            "rare wood": pool_items.Rare_wood(),
            "herbs": pool_items.Herbs(),
            "cinnamon": pool_items.Cinnamon(),
            "cacao beans": pool_items.Cacao_beans(),
            "axe": pool_items.Axe()
        }
    
    def forage(self):
        if random.randint(0,100) < self.success_chance:
            roll = random.randint(1,100)
            self.atempts += 1
            self.success_chance = 100 * ((1 - .06) ** self.atempts)
            if roll >= 95 and self.axes > 0:
                self.axes += -1
                return self.item_pool["axe"]
            else:
                key_list = list(self.item_pool.keys())
                key_list.remove("axe")
                return self.item_pool[random.choice(key_list)]  
        else:
            return None
    

class BeachFishing:
    def __init__(self):
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    def fish(self):
        print("You begin fishing, when you feel a bite on the line, type the letter as quickly as possible")
        wait = random.randint(5,30) / 10
        time.sleep(wait)
        time1 = time.time()
        correct_letter = random.choice(self.alphabet)
        user_input = input(f'You got a bite quick type {correct_letter}: ')
        time2 = time.time()
        try:
            if (time2 - time1) < 4 and user_input == correct_letter:
                return pool_items.Fish()
            else:
                return None
        except:
            return None
        
