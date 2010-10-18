import utils

def add(actions=0, cards=0, money="0", points=0):
    def func(gameState, actions=actions, cards=cards, money=money, points=points):
        gameState.players[gameState.currentPlayer].actions += actions
        gameState.players[gameState.currentPlayer].draw(cards)
        gameState.players[gameState.currentPlayer].money = \
            utils.addMoney(gameState.players[gameState.currentPlayer].money, money)
        gameState.players[gameState.currentPlayer].points += points
    
    return func
