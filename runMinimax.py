import tictactoe
import minimax
import random

# This evaluation function takes up the number of mini wins of 'x' minus
# the number of mini wins of 'o'
def evalFn(gameState):
	return float('inf')*gameState.getWinner() + sum(sum(wins) for wins in gameState.getMiniWins())


# Simulates game to completion
winner1 = 0
winner_1 = 0
agent = minimax.AlphaBetaAgent(evalFn, 2)

for i in range(100):
	myGame = tictactoe.Game()
	myGame.currPlayer = 1
	count = 0
	while(myGame.getMoves() and not myGame.isEnd()):
		if count % 2 == 0 or count < 2:
			moves = myGame.getMoves()
			i = random.randint(0,len(moves)-1)
			myGame.move(moves[i])
		else:
			action = agent.getAction(myGame)
			myGame.move(action)
		count += 1
	print 'Winner: ', myGame.getWinner()
	if myGame.getWinner() == 1:
		winner1 += 1
	elif myGame.getWinner() == -1:
		winner_1 += 1

print 'x won', winner1, 'games, o won', winner_1, 'games'