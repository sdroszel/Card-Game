import random


class Card:
    def __init__(self, number, typ):
        self.number = number
        self.type = typ

    def show(self):
        print(self.number, "of", self.type)

    def get_card_number(self):
        return self.number


class Deck:
    def __init__(self):
        self.list = []
        for x in range(0, 4):
            for y in range(0, 13):
                if x == 0:
                    typ = "hearts"
                elif x == 1:
                    typ = "diamonds"
                elif x == 2:
                    typ = "spades"
                elif x == 3:
                    typ = "clubs"
                else:
                    typ = ""

                if y == 10:
                    num = "Jack"
                elif y == 11:
                    num = "Queen"
                elif y == 12:
                    num = "King"
                else:
                    num = y + 1
                self.list.append(Card(num, typ))

    def show_deck(self):
        print()
        for x in self.list:
            x.show()
        print()

    def get_card_number(self, index):
        return self.list[index].get_card_number()

    def shuffle_deck(self):
        random.shuffle(self.list)
