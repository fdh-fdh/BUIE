import random
from card_Repository import cardRepo


class player:
    def __init__(self,name):
        self.name = name
        self.Mycard = []
        print("Hi my name is ", self.name)

    def __repr__(self):
        print(self.Mycard, sep="  ")


    def play_card(self, cardrepo: cardRepo):
        # "Erstbeste" karte, was heißt das?
        for i in self.Mycard:
            if self.Mycard[i].color == cardrepo.table.color or self.Mycard[i].number == cardrepo.table.number:
                cardrepo.table = self.Mycard[i]
                del self.Mycard[i]
                cardrepo.cards.append(self.Mycard[i])
                print("Hand out the card : " + self.Mycard[i])
                break

            else:
                self.get_penalty_card(cardrepo)
                print("Pass")
                break

    def get_penalty_card(self,cardrepo: cardRepo):
        a = random.randint
        del cardrepo.cards[a]
        self.Mycard.append(a)
        print("")

    def test_player_won(self):
        return self.Mycard == []

    def print_my_cards(self, n):
        # n is the number of the card at the beginning of the game.
        for i in range(1, n):
            repr(self.Mycard[i])

    def print_cards(self):
        print(self.name + " have these cards")
        for i in self.Mycard:
            print(repr(self.Mycard[i]))



