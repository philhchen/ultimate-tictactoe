import tictactoe
import minimax
import random

# Demo of tictactoe.py
myGame = tictactoe.Game()

# Simulates 20 random moves
for count in range(40):
	moves = myGame.getMoves()
	i = random.randint(0,len(moves)-1)
	myGame.move(moves[i])
print 'Big board after 20 moves:'
myGame.printBoard()
print 'Mini wins after 20 moves: '
myGame.printBoard(2)
print 'Winner: ', myGame.getWinner(), '\n\n'

# Plays game to completion
while(myGame.getMoves() and not myGame.isEnd()):
	moves = myGame.getMoves()
	i = random.randint(0,len(moves)-1)
	myGame.move(moves[i])
print 'Big board after completion:'
myGame.printBoard()
print 'Mini wins after completion: '
myGame.printBoard(2)
print 'Winner: ', myGame.getWinner()

# Simulates game to completion
myGame = tictactoe.Game()
while(myGame.getMoves() and not myGame.isEnd()):
	if count % 2 == 0:
		moves = myGame.getMoves()
		i = random.randint(0,len(moves)-1)
		myGame.move(moves[i])
	else:
		evalFn = lambda gameState: 1000*gameState.getWinner() if gameState.isEnd() else sum(sum(wins) for wins in gameState.miniWins) # Replace later with better one
		agent = minimax.AlphaBetaAgent(evalFn)
		action = agent.getAction(myGame)
		print action
		myGame.move(action)
print 'Big board after completion:'
myGame.printBoard()
print 'Mini wins after completion: '
myGame.printBoard(2)
print 'Winner: ', myGame.getWinner(), '\n\n'

'''
# Demo of minimax.py
evalFn = lambda gameState: gameState.getWinner() if gameState.isEnd() else sum(sum(wins) for wins in gameState.miniWins) # Replace later with better one
agent = minimax.AlphaBetaAgent(evalFn)
g = tictactoe.Game()
print agent.getAction(g)
'''
