import random, copy

# Player -1 is o, +1 is x
class Game:
	def __init__(self, dim=3):
		self.dim = dim
		self.board = [[0 for i in range(self.dim*self.dim)] for j in range(self.dim*self.dim)]
		self.miniWins = [[0 for i in range(self.dim)] for j in range(self.dim)]
		self.currPlayer = -1 + 2*random.randint(0,1)
		self.validMoves = [(x,y) for x in range(self.dim*self.dim) for y in range(self.dim*self.dim)]
		self.winner = 0

	def getMoves(self):
		return self.validMoves

	def getCurrPlayer(self):
		return self.currPlayer

	def getMiniWins(self):
		return self.miniWins

	def getBoard(self):
		return self.board

	def isEnd(self):
		return self.winner != 0

	def getWinner(self):
		return self.winner

	def generateSuccessor(self, action):
		newGame = copy.deepcopy(self)
		newGame.move(action)
		return newGame

	# Option = 1: 9x9 board
	# Option = 2: self.dimxself.dim board of mini wins
	def printBoard(self, option=1):
		board = self.board if option == 1 else self.miniWins
		for i in range(len(board)):
			row = board[i]
			strrow = []
			for player in row:
				if player == -1:
					strrow.append('o')
				elif player == 1:
					strrow.append('x')
				else:
					strrow.append('_')
			strrow = ' '.join(strrow)
			strrow2 = ''
			for j in range(self.dim):
				strrow2 = strrow2 + strrow[2*self.dim*j : 2*self.dim*(j+1)] + ' '
			print strrow2
			if (i + 1) % self.dim == 0:
				print

	def move(self,pos):
		if not pos in self.validMoves:
			raise Exception("Invalid Move")
		self.board[pos[0]][pos[1]] = self.currPlayer
		self.updateMiniWinners(pos)
		self.updateWinner()
		self.updateValidMoves(pos)
		self.currPlayer = -self.currPlayer

	def updateValidMoves(self,pos):
		self.validMoves = []
		r0 = pos[0] % self.dim
		c0 = pos[1] % self.dim
		for dr in range(self.dim):
			for dc in range(self.dim):
				r = self.dim*r0 + dr
				c = self.dim*c0 + dc
				if self.board[r][c] == 0:
					self.validMoves.append((r,c))

	# Updates the grid specifying which mini-boards have been won by which players
	def updateMiniWinners(self,pos):
		r0 = pos[0]/self.dim
		c0 = pos[1]/self.dim
		if self.miniWins[r0][c0] == 0:
			for dr in range(self.dim):
				if self.board[self.dim*r0 + dr][self.dim*c0] != 0:
					success = True
					for dc in range(self.dim):
						success = success and self.board[self.dim*r0 + dr][self.dim*c0] == self.board[self.dim*r0 + dr][self.dim*c0 + dc]
					if success:
						self.miniWins[r0][c0] = self.currPlayer
						return
			for dc in range(self.dim):
				if self.board[self.dim*r0][self.dim*c0 + dc] != 0:
					success = True
					for dr in range(self.dim):
						success = success and self.board[self.dim*r0][self.dim*c0 + dc] == self.board[self.dim*r0 + dr][self.dim*c0 + dc]
					if success:
						self.miniWins[r0][c0] = self.currPlayer
						return
			if self.board[self.dim*r0][self.dim*c0] != 0:
				success = True
				for drdc in range(self.dim):
					success = success and self.board[self.dim*r0][self.dim*c0] == self.board[self.dim*r0 + drdc][self.dim*c0 + drdc]
				if success:
					self.miniWins[r0][c0] = self.currPlayer
					return
			if self.board[self.dim*(r0 + 1) - 1][self.dim*c0] != 0:
				success = True
				for dc in range(1, self.dim):
					success = success and self.board[self.dim*(r0 + 1) - 1][self.dim*c0] == self.board[self.dim*(r0 + 1) - 1 - dc][self.dim*c0 + dc]
				if success:
					self.miniWins[r0][c0] = self.currPlayer
					return

	def updateWinner(self):
		if self.winner == 0:
			for r in range(self.dim):
				success = self.miniWins[r][0] != 0
				for c in range(1, self.dim):
					success = success and self.miniWins[r][0] == self.miniWins[r][c]
				if success:
					self.winner = self.miniWins[r][0]
					return

			for c in range(self.dim):
				success = self.miniWins[0][c] != 0
				for r in range(1, self.dim):
					success = success and self.miniWins[0][c] == self.miniWins[r][c]
				if success:
					self.winner = self.miniWins[0][c]
					return

			success = self.miniWins[0][0] != 0
			for rc in range(1, self.dim):
				success = success and self.miniWins[0][0] == self.miniWins[rc][rc]
			if success:
				self.winner = self.miniWins[0][0]
				return

			success = self.miniWins[self.dim - 1][0] != 0
			for c in range(1, self.dim):
				success = success and self.miniWins[self.dim - 1][0] == self.miniWins[self.dim - 1 - c][c]
			if success:
				self.winner = self.miniWins[self.dim - 1][0]

