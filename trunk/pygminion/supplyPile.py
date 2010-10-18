class SupplyPile:
    def __init__(self, card, numCards=10):
        self.pile = numCards*[card]
        self.card = card
    
    def cost(self):
        if not self.isEmpty():
            return self.pile[0].cost
        # Empty pile:
        return "9999"
    
    def isEmpty(self):
        return len(self.pile) == 0
    
    def buy(self):
        if not self.isEmpty():
            return self.pile.pop(0)
        else:
            raise ValueError
