import DQNagent
import tictactoe
import minimax
import random

NUM_ITERS = 30
DIM = 3
BATCH_SIZE = 32
NUM_EPSIODES = 100

# Test function to compare algorithmic agent against random agent in 50 games
def test(agent):
	wins1 = 0
	wins_1 = 0
	for i in range(50):
		myGame = tictactoe.Game(DIM)
		count = 0
		nnPlayer = myGame.getCurrPlayer()
		while(not myGame.isEnd()):
			if count % 2 == 1:
				moves = myGame.getMoves()
				i = random.randint(0, len(moves) - 1)
				myGame.move(moves[i])
			else:
				action = agent.getAction(myGame)
				myGame.move(action)
			count += 1
		if myGame.getWinner() == nnPlayer:
			wins1 += 1
		elif myGame.getWinner() == -nnPlayer:
			wins_1 += 1
	print('{} wins to {} losses'.format(wins1, wins_1))

# Trains the neural net and tests against a random agent after every batch
def run():
	agent = DQNagent.DQNagent(DIM)

	for e in range(1, NUM_EPSIODES+1):
		for i in range(1, NUM_ITERS+1):
			myGame = tictactoe.Game(DIM)
			state = [myGame.getBoard().reshape((1, DIM*DIM, DIM*DIM, 1)),
					myGame.getMiniWins().reshape((1, DIM, DIM))]

			while(not myGame.isEnd()):
				action = agent.getAction(myGame)
				myGame.move(action)
				next_state = [myGame.getBoard().reshape((1, DIM*DIM, DIM*DIM, 1)),
								myGame.getMiniWins().reshape((1, DIM, DIM))]
				winner = myGame.getWinner()

				agent.remember(state, next_state, winner)

				state = next_state

			agent.replay(BATCH_SIZE)

		print("episode: {}/{}, epsilon: {}".format(e, NUM_EPSIODES, agent.epsilon))
		test(agent)

run()

