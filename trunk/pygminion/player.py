import cards

class Player:
    """A Dominion player."""
    
    def __init__(self, name, initialCards=None):
        self.name = name
        
        # We start with the cards in the discard pile.
        # They'll be shuffled to create the deck.
        
        if initialCards: self.discardPile = initialCards
        else:            self.discardPile = [cards.copper]*7 + [cards.estate]*3
        
        # Probably not necessary here, more to create a list
        
        self.points  = 0
        self.money   = 0
        self.buys    = 0
        self.actions = 0
        self.cards   = 0
        
        self.cardsInPlay = []
        self.durationCards = []
        self.deck = []
        self.hand = []
    
    def draw(self, numCards):
        while numCards:
            try:
                self.hand.append(self.deck.pop(0))
                numCards -= 1
            except IndexError:
                if len(self.discardPile) < 1:
                    print "*** DEBUG: %s can't draw %s cards.  " + \
                          "Deck: %s, hand: %s, discard: %s" % (self.name, len(self.deck),
                                                               len(self.hand), len(self.discardPile))
                    return True
                else:
                    print "*** DEBUG: Shuffling %s's discard pile into a new deck..." % self.name
                    random.shuffle(self.discardPile)
                    self.hand = list(self.discardPile)
                    self.discardPile = []
                
    def initTurn(self):
        self.actions = 1
        self.buys    = 1
        
        for card in durationCards:
            card.cbInitTurn()
