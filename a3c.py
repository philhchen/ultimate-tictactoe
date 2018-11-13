import tensorflow as tf
from tensorflow.keras import layers
import collections

class ActorCriticModel(tf.keras.Model):
	def __init__(self, state_size, action_size):
		super(ActorCriticModel, self).__init__()
		# Hyperparameters
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
	def __init__(self, dim):
		self.state1_size = (dim**2, dim**2, 1)
		self.state2_size = (dim, dim)
		self.action_size = dim**2

		self.memory = collections.deque(maxlen=2000)
		self.gamma = 0.95    # discount rate
		self.epsilon = 1.0  # exploration rate
		self.epsilon_min = 0.01
		self.epsilon_decay = 0.999
		self.lr = 0.0001

		self.model = ActorCriticModel(self.state1_size, self.action_size)
		self.model.compile(optimizer=tf.train.AdamOptimizer(self.lr), loss='binary_crossentropy')

	def getAction():

	def remember(self, state, next_state, winner):
		self.memory.append((state, next_state, winner))

a = A2CAgent(3)
