import random

card_suits = ["♠", "♥", "♦", "♣"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

def make_card_picture(value=None, card_suit=None):

    return f"""
┌─────────┐
│{value:<2}       │
│         │
│    {card_suit}    │
│         │
│       {value:>2}│
└─────────┘
"""

def create_deck():
    deck = []

    for suit in card_suits:
        for card in values:
            deck.append({
                "card": card,
                "suit": suit,
                "value": cards[card],
                "picture": make_card_picture(card,suit)
            })
    random.shuffle(deck)

    return deck

def draw_card(hand,deck):
    hand[len(hand)] = deck.pop()