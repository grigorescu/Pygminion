#!/usr/bin/env python

import generic
import simpleCBs

# Basic Treasures

copper   = generic.card("Copper", "0", treasure=True, supply=False, cbPlay=simpleCBs.add(money="1"))
silver   = generic.card("Silver", "3", treasure=True, supply=False, cbPlay=simpleCBs.add(money="2"))
gold     = generic.card("Gold", "6", treasure=True, supply=False, cbPlay=simpleCBs.add(money="3"))
platinum = generic.card("Platinum", "9", treasure=True, supply=False, cbPlay=simpleCBs.add(money="5"))
potion   = generic.card("Potion", "4", treasure=True, supply=False, cbPlay=simpleCBs.add(money="p"))

# Basic VPs

estate   = generic.card("Estate", "2", victory=True, supply=False, cbEndCount=simpleCBs.add(points=1))
duchy    = generic.card("Duchy", "5", victory=True, supply=False, cbEndCount=simpleCBs.add(points=3))
province = generic.card("Province", "8", victory=True, supply=False, cbEndCount=simpleCBs.add(points=6))
colony   = generic.card("Colony", "11", victory=True, supply=False, cbEndCount=simpleCBs.add(points=9))
curse    = generic.card("Curse", "0", supply=False, cbEndCount=simpleCBs.add(points=-1))

# Base Set

festival = generic.card("Festival", "5", action=True, cbPlay=lambda : {'actions': '+2', 'money': '+2',
                                                                       'buys': '+1'})
laboratory = generic.card("Laboratory", "5", action=True, cbPlay=lambda : {'cards': '+2', 'actions': '+1'})
market = generic.card("Market", "5", action=True, cbPlay=lambda : {'actions': '+1', 'money': '+1',
                                                                       'buys': '+1', 'cards': '+1'})
smithy = generic.card("Smithy", "4", action=True, cbPlay=lambda : {'cards': '+3'})
village = generic.card("Village", "3", action=True, cbPlay=lambda : {'cards': '+1', 'actions': '+2'})
woodcutter = generic.card("Woodcutter", "3", action=True, cbPlay=lambda : {'money': '+2', 'buys': '+1'})

# Adventurer: $6; Action; Reveal from deck until you get 2 treasures; discard all drawn non-treasures
# Bureaucrat: $4; Action/Attack; put 1 silver from supply on top of your deck; force opponents to put 1 VP card from hand on top of their deck
# Cellar: $2; Action; +1 Action; Discard any number of cards; draw +1 Card per discard
# Chancellor: $3; Action; +2 Coin; You may put your deck into your discard pile
# Chapel: $2; Action; Trash up to 4 cards from hand
# Council Room: $5; Action; +4 cards; Opponents +1 Card; +1 Buy
# Gardens: $4; 1 VP for every 10 cards in deck {this is a VP card, use same # of cards as normal VP cards}
# Library: $5; Action; Draw to seven in hand, putting action cards of your choice aside. Discard those actions. {You may keep actions you want in your hand.}
# Militia: $4; Action/Attack; Opponents discard down to 3 cards; +2 Coins
# Mine: $5; Action; Trash a Treasure - gain a treasure of cost up to three higher than cost of card trashed.
# Moat: $2; Action/Reaction: Prevent Attacks on other player's turns; +2 Cards
# Money Lender: $4; Action; Trash a copper for +3 coins during buy phase
# Remodel: $4; Action; Trash a card, gain a card worth up to that card + $2
# Spy: $4; Action/Attack; +1 card; +1 action; All players flip top card of deck, you choose to put card to discard or back on top of deck
# Thief: $4; Action/Attack: Opponents reveal top two cards of deck and trash one treasure, discarding all non trashed cards. Thief picks card to trash if there are two treasures revealed. Thief then takes as many of the treasures just trashed as they like.
# Throne Room: $4; Action; Play another Action in hand twice
# Witch: $5; Action/Attack; +2 Cards; Give everyone else a curse (-1 VP) on their discard pile
# Workshop: $3; Action; Get a card worth up to $4 from Supply
