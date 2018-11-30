import tictactoe
from minimax import AlphaBetaAgent
from mcts import MCTSagent

class HybridAgent:
	def __init__(self):
		self.mcts = MCTSagent(itermax=500)
		self.minimax = AlphaBetaAgent(depth=3)

	def getAction(self, gameState):
		if gameState.getNumMoves() < 30:
			return self.mcts.getAction(gameState)
		else:
			return self.minimax.getAction(gameState)