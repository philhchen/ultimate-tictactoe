import DQNagent
import tictactoe
import minimax

NUM_ITERS = 100
DIM = 3
BATCH_SIZE = 32
NUM_EPSIODES = 100

def run():
	agent = DQNagent.DQNagent((DIM*DIM, DIM*DIM, 1))

	for e in range(1, NUM_EPSIODES+1):
		for i in range(1, NUM_ITERS+1):
			myGame = tictactoe.Game(DIM)
			state = myGame.getBoard().reshape((1, DIM*DIM, DIM*DIM, 1))

			while(not myGame.isEnd()):
				action = agent.act(myGame)
				myGame.move(action)
				next_state = myGame.getBoard().reshape((1, DIM*DIM, DIM*DIM, 1))
				winner = myGame.getWinner()

				agent.remember(state, next_state, winner)

				state = next_state

			agent.replay(BATCH_SIZE)

		print("epsilode: {}/{}".format(e, NUM_EPSIODES))
run()