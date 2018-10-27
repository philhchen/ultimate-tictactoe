import random, copy

# Player -1 is o, +1 is x
class Game:
	def __init__(self):
		self.board = [[0 for i in range(9)] for j in range(9)]
		self.miniWins = [[0 for i in range(3)] for j in range(3)]
		self.currPlayer = -1 + 2*random.randint(0,1)
		self.validMoves = [(x,y) for x in range(9) for y in range(9)]
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
	# Option = 2: 3x3 board of mini wins
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
			print strrow[:6] + ' ' + strrow[6:12] + ' ' + strrow[12:]
			if i % 3 == 2:
				print

	def move(self,pos):
		isValid = False
		for move in self.validMoves:
			if move == pos:
				isValid = True
				break
		if not isValid:
			raise Exception("Invalid Move")
		self.board[pos[0]][pos[1]] = self.currPlayer
		self.updateMiniWinners(pos)
		self.updateWinner()
		self.updateValidMoves(pos)
		self.currPlayer = -self.currPlayer

	def updateValidMoves(self,pos):
		self.validMoves = []
		r0 = pos[0] % 3
		c0 = pos[1] % 3
		for dr in range(3):
			for dc in range(3):
				r = 3*r0 + dr
				c = 3*c0 + dc
				if self.board[r][c] == 0:
					self.validMoves.append((r,c))

	# Updates the grid specifying which mini-boards have been won by which players
	def updateMiniWinners(self,pos):
		r0 = pos[0]/3
		c0 = pos[1]/3
		if self.miniWins[r0][c0] == 0:
			for dr in range(3):
				if self.board[3*r0 + dr][3*c0] != 0:
					if self.board[3*r0 + dr][3*c0] == self.board[3*r0 + dr][3*c0 + 1] and self.board[3*r0 + dr][3*c0] == self.board[3*r0 + dr][3*c0 + 2]:
						self.miniWins[r0][c0] = self.currPlayer
						return
			for dc in range(3):
				if self.board[3*r0][3*c0 + dc] != 0:
					if self.board[3*r0][3*c0 + dc] == self.board[3*r0 + 1][3*c0 + dc] and self.board[3*r0][3*c0 + dc] == self.board[3*r0 + 2][3*c0 + dc]:
						self.miniWins[r0][c0] = self.currPlayer
						return
			if self.board[3*r0][3*c0] != 0:
				if self.board[3*r0][3*c0] == self.board[3*r0 + 1][3*c0 + 1] and self.board[3*r0][3*c0] == self.board[3*r0 + 2][3*c0 + 2]:
					self.miniWins[r0][c0] = self.currPlayer
					return
			if self.board[3*r0 + 2][3*c0] != 0:
				if self.board[3*r0 + 2][3*c0] == self.board[3*r0 + 1][3*c0 + 1] and self.board[3*r0 + 2][3*c0] == self.board[3*r0][3*c0 + 2]:
					self.miniWins[r0][c0] = self.currPlayer
					return

	def updateWinner(self):
		if self.winner == 0:
			for r in [0, 1, 2]:
				if self.miniWins[r][0] != 0 and self.miniWins[r][0] == self.miniWins[r][1] and self.miniWins[r][0] == self.miniWins[r][2]:
					self.winner = self.miniWins[r][0]
					return
			for c in [0, 1, 2]:
				if self.miniWins[0][c] != 0 and self.miniWins[0][c] == self.miniWins[1][c] and self.miniWins[0][c] == self.miniWins[2][c]:
					self.winner = self.miniWins[0][c]
					return
			if self.miniWins[0][0] != 0 and self.miniWins[0][0] == self.miniWins[1][1] and self.miniWins[0][0] == self.miniWins[2][2]:
				self.winner = self.miniWins[0][0]
				return
			if self.miniWins[2][0] != 0 and self.miniWins[2][0] == self.miniWins[1][1] and self.miniWins[2][0] == self.miniWins[0][2]:
				self.winner = self.miniWins[2][0]

