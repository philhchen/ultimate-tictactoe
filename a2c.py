import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, activations
import collections
import tictactoe

tf.enable_eager_execution()


class ActorCriticModel(tf.keras.Model):
	def __init__(self, state_size, action_size):
		super(ActorCriticModel, self).__init__()
		self.state_size = state_size
		self.action_size = action_size

		# Convolutional base
		self.conv = layers.Conv2D(24, (3,3), activation='relu', strides=(3,3))
		self.flatten = layers.Flatten()

		# Value head
		self.dense_1 = layers.Dense(12, activation='relu')
		self.values = layers.Dense(1, activation='relu')

		# Policy head
		self.dense_2 = layers.Dense(16, activation='relu')
		self.policy_logits = layers.Dense(action_size)

	def call(self, inputs):
		x = self.conv(inputs)
		x = self.flatten(x)

		values = self.dense_1(x)
		values = self.values(values)

		logits = self.dense_2(x)
		logits = self.policy_logits(logits)

		return logits, values

class A2CAgent():
	def __init__(self, dim=3):
		self.state_size = (dim**2, dim**2, 4)
		self.action_size = dim**2

		# Hyperparameters
		self.memory = collections.deque(maxlen=2000)
		self.gamma = 0.95    # discount rate
		self.epsilon = 1.0  # exploration rate
		self.epsilon_min = 0.01
		self.epsilon_decay = 0.999
		self.lr = 0.0001

		self.model = ActorCriticModel(self.state_size, self.action_size)
		self.model.compile(optimizer=tf.train.AdamOptimizer(self.lr), loss='binary_crossentropy')

	def getAction(self, game):
		logits, _ = self.model(tf.convert_to_tensor(self.extractState(game)))
		probs = activations.softmax(logits)
		action = np.random.choice(self.action_size, p=probs.numpy()[0])
		while action >= len(game.getMoves()):
			action = np.random.choice(self.action_size, p=probs.numpy()[0])
		return game.getMoves()[action]

	def extractState(self, game):
		state = np.zeros((1, self.state_size[0], self.state_size[1], self.state_size[2]))
		state[0,:,:,0] = (game.getBoard() == 1)
		state[0,:,:,1] = (game.getBoard() == -1)
		state[0,:,:,2] = (game.getCurrPlayer() == 1)
		for move in game.getMoves():
			state[0,move[0],move[1],3] = 1
		return state

	def remember(self, state, next_state, winner):
		self.memory.append((state, next_state, winner))

class Train():
	def __init__(self, dim=3):
		self.dim = dim
		self.agent = A2CAgent(self.dim)
		self.gamma = 0.95

	def computeLoss(self):
		a = 0

	def step(self):
		myGame = tictactoe.Game()
		tempMemory = []
		while not myGame.isEnd():
			state = self.agent.extractState(myGame)
			action = self.agent.getAction(myGame)

			myGame.move(action)
			newState = self.agent.extractState(myGame)

			tempMemory.append((state, newState))
		
		# Store states/newstates in memory
		for i, (state, newState) in enumerate(tempMemory):
			discounted_win = myGame.getWinner() * (self.gamma**(len(tempMemory) - i - 1))
			winProb = (1+discounted_win)/2
			self.agent.remember(state, newState, winProb)

		with tf.GradientTape() as tape:
			total_loss = self.computeLoss()

	def run(self):
		agent = A2CAgent(3)
		self.step()

t = Train()
t.run()
