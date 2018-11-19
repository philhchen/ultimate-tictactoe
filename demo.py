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
print('Big board after 20 moves:')
myGame.printBoard()
print('Mini wins after 20 moves: ')
myGame.printBoard(2)
print('Winner: ', myGame.getWinner(), '\n\n')

# Plays game to completion
while(myGame.getMoves() and not myGame.isEnd()):
	moves = myGame.getMoves()
	i = random.randint(0,len(moves)-1)
	myGame.move(moves[i])
print('Big board after completion:')
myGame.printBoard()
print('Mini wins after completion: ')
myGame.printBoard(2)
print('Winner: ', myGame.getWinner())

