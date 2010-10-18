#!/usr/bin/env python

import cards
import random
import utils

class Player:
    """A Dominion player."""
    
    def __init__(self, name, initialCards=None, actionFunc=None, buyFunc=None):
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
        
        self.draw(5)
        
        
        if not actionFunc:
            def doFirstAction(self):
                for card in self.hand:
                    if card.action:
                        print "*** DEBUG: Playing %s." % card.name
                        card.cbPlay()
            self.actionFunc = doFirstAction
            
        if not buyFunc:
            def randomBuy(self, options):
                choice = random.choice(options)
                print "*** DEBUG: Buying %s." % choice.card.name
                self.discardPile.append(choice.buy())
            self.buyFunc = randomBuy


    
    def draw(self, numCards):
        while numCards:
            try:
                self.hand.append(self.deck.pop(0))
                numCards -= 1
            except IndexError:
                if len(self.discardPile) < 1:
                    print "*** DEBUG: %s can't draw %s cards.  Deck: %s, hand: %s, discard: %s" % (self.name, numCards, len(self.deck), len(self.hand), len(self.discardPile))
                    return True
                else:
                    print "*** DEBUG: Shuffling %s's discard pile into a new deck..." % self.name
                    random.shuffle(self.discardPile)
                    self.deck = list(self.discardPile)
                    self.discardPile = []
                
    def turn(self, gameState):
        self.actions = 1
        self.buys    = 1
        self.money   = "0"
        
        for card in self.durationCards:
            card.cbInitTurn(gameState)
        
        # Action
        
        print "*** DEBUG: %s's turn.  Hand: %s." % (self.name, self.hand)
        self.actionFunc(self)
            
        # Buy
        
        for card in self.hand:
            if card.treasure:
                card.cbPlay(gameState)
        
        options = []
        for supply in gameState.supplies:
            if not supply.isEmpty():
                if utils.cmpMoney(self.money, supply.cost()) >= 0:
                    options.append(supply)
        
        self.buyFunc(self, options)            
        
        # Cleanup
        self.discardPile += self.hand
        self.hand = []
        self.draw(5)

class SupplyPile:
    def __init__(self, card, numCards=10):
        self.pile = numCards*[card]
        self.card = card
    
    def __repr__(self):
        return "%dx[%s (%s)]" % (len(self.pile), self.card.name, self.cost())
    
    def cost(self):
        return self.card.cost
    
    def isEmpty(self):
        return len(self.pile) == 0
    
    def buy(self):
        if not self.isEmpty():
            
            return self.pile.pop(0)
        else:
            raise ValueError

class Game:
    """A Dominion game."""
    
    def __init__(self, numPlayers=2, players=None, supplyCards=None, potions=False, coloniesPlatinums=False):
        if players:
            self.players = players
        else:
            self.players = []
            for i in range(numPlayers):
                self.players.append(Player("Player %s" % (i + 1)))
        
        vpCards = [0, 0, 8, 12, 12, 15, 18][numPlayers]
        
        self.supplies = [SupplyPile(cards.copper, 60), SupplyPile(cards.silver, 60), SupplyPile(cards.gold, 60),
                         SupplyPile(cards.estate, vpCards), SupplyPile(cards.duchy, vpCards), SupplyPile(cards.province, vpCards)]
        self.trash = []
        self.currentPlayer = 0
        
    def isGameOver(self):
        emptySupplies = 0
        for supply in self.supplies:
            if supply.isEmpty():
                if supply.card == cards.province: return True
                if supply.card == cards.colony:   return True
                emptySupplies += 1
        if len(self.players) <= 3:
            return emptySupplies >= 3
        else:
            return emptySupplies >= len(self.players) - 1
    
    def next(self):
        while not self.isGameOver():
            yield self.players[self.currentPlayer].turn(self)
            self.currentPlayer += 1
            if self.currentPlayer >= len(self.players):
                self.currentPlayer = 0
        
        raise StopIteration
    
    def pointTotals(self):
        for i in range(len(self.players)):
            player = self.players[i]
            self.currentPlayer = i
            all_cards = player.hand + player.discardPile + player.deck + player.cardsInPlay + player.durationCards
            for card in all_cards:
                card.cbEndCount(self)
            print "%s: %d -- %s" % (player.name, player.points, all_cards)

