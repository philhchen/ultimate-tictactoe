import mcts
import tictactoe
import minimax
import random

wins = 0
for i in range(100):
	agent = mcts.MCTSagent(100)
	myGame = tictactoe.Game(3)
	count = 0
	nnPlayer = myGame.getCurrPlayer()
	while(not myGame.isEnd()):
		if count % 2 == 1:
			myGame.move(myGame.getRandomMove())
		else:
			action = agent.getAction(myGame)
			myGame.move(action)
		count += 1
		
	print('Player:', nnPlayer, 'Winner: ', myGame.getWinner())
	if nnPlayer == myGame.getWinner():
		wins += 1
print('Wins: ', wins)

