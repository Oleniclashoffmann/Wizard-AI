class Card: 
    def __init__(self, suit, value): 
        self.suit = suit #"Red", "Yellow", "Green", "Blue"
        self.value = value # 1-13, or Wizard/Fool
    
    def __repr__(self):
        return f"{self.value} of {self.suit}" if self.suit else str(self.value)
    
    