import tictactoe
import random

class AlphaBetaAgent():
	def __init__(self, evalFn, depth = '4'):
		self.index = 0 # Pacman is always agent index 0
		self.evaluationFunction = evalFn
		self.depth = int(depth)

	def getAction(self, gameState):
		"""
		Returns the minimax action using self.depth and self.evaluationFunction
		"""
		def recurse(gameState, player, depth, alpha, beta):
			if gameState.isEnd() or depth == 0:
				return (self.evaluationFunction(gameState), 'END')

			moves = gameState.getMoves()
			if player == 1:
				ans = (-float('Inf'),'NA')
				for action in moves:
					ans = max(ans, (recurse(gameState.generateSuccessor(action), 
							-player, depth, alpha, beta)[0], action))
					alpha = max(alpha, ans)
					if alpha >= beta:
						break
				return alpha
			else:
				ans = (float('Inf'),'NA')
				for action in moves:
					ans = min(ans, (recurse(gameState.generateSuccessor(action), 
							-player, depth - 1, alpha, beta)[0], action))
					beta = min(beta, ans)
					if alpha >= beta:
						break
				return beta
		alph0 = (-float('Inf'), 'NA')
		beta0 = (+float('Inf'), 'NA')
		utility, action = recurse(gameState, 0, self.depth, alph0, beta0)
		return action
	# END_YOUR_CODE
