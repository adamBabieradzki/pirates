import game.items as items

class money(items.Item()):
    def __init__(self):
        super().__init__("Coin Purse",1)
        self.contents = {"\u00A3": 0, "s": 0, "d": 0}
        self.verb = "value"