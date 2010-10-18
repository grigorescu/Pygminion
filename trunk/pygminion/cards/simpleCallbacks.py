def add(gameState, actions=0, cards=0, money=0, points=0):
    gameState.players[gameState.currentPlayer].actions += actions
    gameState.players[gameState.currentPlayer].draw(cards)
    gameState.players[gameState.currentPlayer].actions += money
    gameState.players[gameState.currentPlayer].actions += points
