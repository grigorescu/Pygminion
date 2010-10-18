#!/usr/bin/env python

class card:
    """Generic Dominion card.  Use as base class."""
    
    def _installCallback(self, function, functionName):
        if function: 
            setattr(self, functionName, function)
        else:
            def emptyCallback(gameState):
                return {}
            setattr(self, functionName, emptyCallback)

    def __init__(self, name, cost, treasure=False, attack=False, reaction=False,
                 victory=False, action=False, duration=False, supply=True,
                 cbBuy=None, cbInitTurn=None, cbPlay=None, cbAttack=None, cbEndCount=None):
        self.name = name; self.cost = cost; self.treasure = treasure; self.attack = attack; 
        self.reaction = reaction; self.victory = victory; self.action = action; self.duration = duration
        
        # Called when you buy this card
        self._installCallback(cbBuy, "cbBuy")
        # Called when your turn starts, and you have this card in front of you (ie duration cards)
        self._installCallback(cbInitTurn, "cbInitTurn")
        # Called when you play this card
        self._installCallback(cbPlay, "cbPlay")
        # Called when another player plays an attack card
        self._installCallback(cbAttack, "cbAttack")
        # Called when you're counting VPs at the end
        self._installCallback(cbEndCount, "cbEndCount")
        
    def __repr__(self):
        data = "$(%s)$ %s" % (self.cost, self.name)
        if self.treasure: data += " - Treasure "
        if self.attack: data += " - Attack"
        if self.reaction: data += " - Reaction"
        if self.victory: data += " - Victory "
        if self.action: data += " - Action"
        if self.duration: data += " - Duration"
        
        return self.name
