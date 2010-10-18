#!/usr/bin/env python

from game import Game

game = Game()
for t in game.next():
    pass
print game.supplies
game.pointTotals()
