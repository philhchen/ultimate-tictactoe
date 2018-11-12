import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras import layers
from keras import optimizers
import collections, random
import tictactoe

class DQNagent:
	def __init__(self, state_size):
		self.state_size = state_size
		self.memory = collections.deque(maxlen=2000)
		self.gamma = 0.95    # discount rate
		self.epsilon = 1.0  # exploration rate
		self.epsilon_min = 0.01
		self.epsilon_decay = 0.995
		self.learning_rate = 0.001
		self.model = self._build_model()

	def _build_model(self):
		# Neural Net for Deep-Q learning Model
		model = Sequential()
		model.add(layers.Conv2D(24, (3,3), activation='relu', 
					strides=(3,3), input_shape=self.state_size))
		model.add(layers.Flatten())
		# model.add(Dense(60, activation='relu'))
		model.add(Dense(16, activation='relu'))
		model.add(Dense(1, activation='tanh'))
		model.compile(loss='binary_crossentropy',
		              optimizer='rmsprop')
		model.summary()
		return model

	def remember(self, state, next_state, winner):
		self.memory.append((state, next_state, winner))

	def getAction(self, game):
		moves = game.getMoves()
		if np.random.rand() <= self.epsilon:
			i = random.randint(0,len(moves)-1)
			return moves[i]
		q = []
		for action in moves:
			board = np.array(game.getBoard())
			board[action] = game.getCurrPlayer()
			board = board.reshape((1, self.state_size[0], self.state_size[1], self.state_size[2]))
			q.append((self.model.predict(board) * game.getCurrPlayer(), action))
		return max(q)[1]

	def replay(self, batch_size):
		minibatch = random.sample(self.memory, batch_size)
		for state, next_state, winner in minibatch:
			target = [[winner]] if winner != 0 else self.gamma * self.model.predict(next_state)
			self.model.fit(state, target, epochs=1, verbose=0)
		if self.epsilon > self.epsilon_min:
			self.epsilon *= self.epsilon_decay

