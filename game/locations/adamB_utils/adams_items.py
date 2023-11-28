import game.items as items

#for casino
class Chip(items.Item):
    def __init__(self,n):
        self.n = n
        super().__init__(f"{self.n} Casino Chip",1)
        
    
    def win_chips(self,amnt):
        self.n += amnt
    
    def lose_chips(self,amnt):
        self.n += -amnt