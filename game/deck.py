class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ["Heearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [(rank, suit) for rank in ranks for suit in suits] # This line creates a list of tuples, where each tuple represents a card in the deck.

    def shuffle(self):
        import random
        random.shuffle(self.cards)