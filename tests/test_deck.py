import unittest
from game.deck import Deck
from pprint import pprint

class TestDeck(unittest.TestCase):
    def test_deck_creation(self): # 'self' is a reference to the current instance of the class and is used to access class attributes and methods.
        deck = Deck() # Create a new instance of the Deck class. Test
        self.assertEqual(len(deck.cards), 52) # Check if the number of cards in the deck is 52.
        print("DECK CREATED:\n")
        pprint(deck.cards)

    def test_shuffle(self):
        deck = Deck()
        initialState = deck.cards.copy()

        deck.shuffle()

        self.assertNotEqual(initialState, deck.cards)
        print("\nDECK SHUFFLED:\n")
        pprint(deck.cards)