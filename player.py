class Player: 
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bid = 0
        self.tricks_won = 0

    def reset(self):
        self.hand = []
        self.bid = 0
        self.tricks_won = 0

    def make_bid(self):
        # Placeholder for agent logic or rule-based logic
        return 0

    def play_card(self, lead_suit=None):
        # Placeholder for playing a card
        return self.hand.pop(0)