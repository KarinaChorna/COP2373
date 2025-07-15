# Karina Chorna
# Programming Exercise 11
# The purpose of this code is to deal a poker hand of 5 cards and prompt the user to replace any cards before
# displaying their hand.

import random

class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in range(4)
                      for rank in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def deal_hand(self, num):
        hand = []
        for _ in range(num):
            hand.append(self.pop_card())
        return hand


def display_hand(hand, label="Your hand"):
    print(f"\n{label}:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")

# replace the chosen cards
def replace_cards(deck, hand, indices_to_replace):
    for i in indices_to_replace:
        hand[i] = deck.pop_card()

def main():
    # initialize and shuffle deck
    deck = Deck()
    deck.shuffle()

    # deal a poker hand of 5 cards
    hand = deck.deal_hand(5)
    display_hand(hand)

    # ask user which cards to replace
    input_str = input("\nEnter card numbers to replace (e.g. 1 2 5) or press Enter to keep all: ").strip()
    if input_str:
        try:
            indices = [int(x) - 1 for x in input_str.split()]
            # make sure the input is valid
            indices = [i for i in indices if 0 <= i < 5]
            replace_cards(deck, hand, indices)
        except ValueError:
            print("Invalid input.")

    # display final hand
    display_hand(hand, label="Your final hand")

if __name__ == "__main__":
    main()
