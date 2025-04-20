from env.card import Card
from env.player import Player
from utils.constants import SUITS, VALUES, SPECIAL_CARDS
import random

class WizardGame:
    def __init__(self, num_players=4):
        self.players = [Player(f"Player {i}") for i in range(num_players)]
        self.deck = []

    def build_deck(self):
        self.deck = [Card(suit, val) for suit in SUITS for val in VALUES]
        self.deck += [Card(None, "Wizard") for _ in range(4)]
        self.deck += [Card(None, "Fool") for _ in range(4)]
        random.shuffle(self.deck)

    def deal_cards(self, round_number):
        for player in self.players:
            player.reset()
            player.hand = [self.deck.pop() for _ in range(round_number)]

    def run_round(self, round_number):
        self.build_deck()
        self.deal_cards(round_number)
        for player in self.players:
            player.bid = player.make_bid()
        # You can add trick logic here next

    def reset(self):
        self.build_deck()
