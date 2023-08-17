from Karte import Card
import random


class cardRepo:
    def __init__(self):
        self.cards= {}
        color = ['red', 'blue', 'yellow', 'green']
        number = range(0,9)
        for i in range(1,100):
            for numbers in number:
                for color in color:
                    self.cards[i]=(Card(color, numbers))
        # die obereste liegende Karte is im "table" gespeichert
        self.table = 0

    def __repr__(self):
        for i in range(len(self.cards)):
            return "cardRepo('"+str(self.cards[i].number)+"','" + self.cards[i].color + ")"

    def handout_card(self, pl):
        if self.cards:
            id = random.randint(0, 99)
            handout_card = self.cards[id]
            del self.cards[id]
            print(repr(handout_card))
            pl.Mycard.append(handout_card)

    def handout_multiple_cards(self, menge: int, pl):
        handout_cards = []
        for i in range(0, menge):
            id = random.randint(0, len(self.cards))
            pl.Mycard.append(self.cards[id])
            del self.cards[id]
        repr(pl)









