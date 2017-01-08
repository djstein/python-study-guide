'''
Deck of cards
52 cards
4 suits
1 of each
randomized deck
'''
from enum import Enum

class Suit(Enum):
    HEARTS = 'HEARTS'
    CLUBS = 'CLUBS'
    DIAMOND = 'DIAMOND'
    SPADE = 'SPADE'


class Card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.played = False

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck():

    def __init__(self):
        self.cards = []
        self.discarded = []

    def create_cards(self):
        for suit in Suit:
            for value in range(1,14):
                card = Card(value, suit)
                print(card)
                self.cards.insert(len(self.cards), card)

    def draw(self):
        drawn_card = self.cards[random.randrange(0, len(cards))]
        return drawn_card


class Hand():

    def __init__(self):
        self.hold = []

deck = Deck()
deck.create_cards()
[print(card) for card in deck.cards]

deck.draw()