import random


class Card:
    suits = {"spades":"\u2660","hearts":"\u2665","diamonds":"\u2666","clubs":"\u2663"}
    faces = [f'{x}' for x in range(2,11,1)] + ["A","J","Q","K"]
    values = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
    def __init__(self,suit,face)->None:
        self.suit = suit
        self.face = face
        self.value = self.values[self.face]
    def declare_ace(self,value:int):
        if self.face == "A":
            self.value = value
    def __repr__(self):
        return f'{self.suits[self.suit]}{self.face}'
    def __str__(self):
        return f'{self.suits[self.suit]}{self.face}'
                 

class Deck:
    def __init__(self):
        self.content = []
        for i in Card.suits.keys():
            for j in Card.faces:
                self.content.append(Card(i,j))
        random.shuffle(self.content)
    def shuffle(self):
        self.content = []
        for i in Card.suits.keys():
            for j in Card.faces:
                self.content.append(Card(i,j))
        random.shuffle(self.content)
    def draw(self):
        if len(self.content) > 0:
            return self.content.pop()
        else:
            self.shuffle()
            self.draw()
        

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = [[],0]
        self.dealer_hand = [[],0]
    def target(self,inp):
        if inp == 1:
            return self.player_hand
        elif inp == 2:
            return self.dealer_hand 
    def draw(self,target,n=1):
        for i in range(n):
            card = self.deck.draw()
            if card.face == "A" and target == 1:
                ace_val = None
                while ace_val == None:
                    while True:
                        try:
                            declare = int(input("You drew an Ace, do you declare 11 or 1:"))
                        except:
                            continue
                        else:
                            break
                    if declare == 11 or declare == 1:
                        ace_val = declare
                card.declare_ace(ace_val)
            elif card.face == "A" and target == 2:
                if self.target(target)[1] > 10: 
                    card.declare_ace(1)
                else: 
                    card.declare_ace(11)
            self.target(target)[0].append(card)
            self.target(target)[1] += card.value
    def printout(self):
        handstring1 = ""
        for i in self.player_hand[0]:
            handstring1 += str(i) + " "
        handstring1 = handstring1 + ":" + str(self.player_hand[1])
        handstring2 = ""
        for i in self.dealer_hand[0]:
            handstring2 += str(i) + " "
        handstring2 = handstring2 + ":" +str(self.dealer_hand[1])
        print(f'Your Hand: {handstring1}')
        print(f'Dealers Hand: {handstring2}')
    def play_game(self):
        self.player_hand = [[],0]
        self.dealer_hand = [[],0]
        self.draw(1,2)
        self.draw(2,2) #player and dealer get 2 cards each
        self.printout()
        win_flag = None
        while True:
            if self.player_hand[1] > 21:
                win_flag = "dealer"
                break
            elif self.dealer_hand[1] > 21:
                win_flag = "player"
                break
            stand = False
            while stand == False:
                print("Dealer: Hit or Stand")
                decision = input(": ")
                while decision not in ["hit","stand","Hit","Stand"]:
                    input(": ")
                if decision == "hit":
                    self.draw(1,1)
                    self.printout()
                    if self.player_hand[1] > 21:
                        win_flag = "dealer"
                        break
                else:
                    print(f"Final Hand Score is {self.player_hand[1]}")
                    stand = True
                    break
            while self.dealer_hand[1] <= 16:
                self.draw(2,1)
                self.printout()
                if self.dealer_hand[1] > 21:
                    if win_flag == None: win_flag = "player"
                    break
            if self.player_hand[1] > self.dealer_hand[1]:
                if win_flag == None: win_flag = "player"
                break
            else:
                if win_flag == None: win_flag = "dealer"
                break
        if win_flag == "player":
            print("You win this hand")
        else:
            print("You Lose this hand")
        return win_flag



if __name__ == "__main__":
    game1 = Game()
    game1.play_game()
    
