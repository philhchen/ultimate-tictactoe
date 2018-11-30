import DQNagent
import tictactoe
import minimax
import random

NUM_ITERS = 10
DIM = 3
BATCH_SIZE = 32
NUM_EPSIODES = 50

# Trains the neural net and tests against a random agent after every batch
def train(agent):
	for e in range(1, NUM_EPSIODES+1):
		for i in range(1, NUM_ITERS+1):
			myGame = tictactoe.Game(DIM)
			state = agent.extractState(myGame)

			tempMemory = []
			while(not myGame.isEnd()):
				action = agent.getAction(myGame)
				myGame.move(action)
				next_state = agent.extractState(myGame)
				winner = myGame.getWinner()

				tempMemory.append((state, next_state))

				state = next_state

			for j, (state, next_state) in enumerate(tempMemory):
				weight = myGame.getWinner() * (agent.gamma**(len(tempMemory) - 1 - j))
				agent.remember(state, next_state, weight)
			
			agent.replay(BATCH_SIZE)
		
		print("episode: {}/{}, epsilon: {}".format(e, NUM_EPSIODES, agent.epsilon))	
		print('Loss:', agent.history.history['loss'][0])
	agent.model.save('dqnModel.h5')

