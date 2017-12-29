# This file will contain the neural network structure
import numpy as np


class Brain:

    def __init__(self):

        # initalise nodes to zero
        self.N0 = np.zeros(49)
        self.N1 = np.zeros(16)
        self.N2 = np.zeros(16)
        self.N3 = np.zeros(7)

        # initalise weights randomly
        self.W1 = (np.random.rand(16,49)*10.0)-5.0
        self.W2 = (np.random.rand(16,16)*10.0)-5.0
        self.W3 = (np.random.rand(7,16)*10.0)-5.0

        # initalise biases randomly
        self.B1 = (np.random.rand(16)*10.0)-5.0
        self.B2 = (np.random.rand(16)*10.0)-5.0
        self.B3 = (np.random.rand(7)*10.0)-5.0

    def evaluate(self, N0):
        self.N0 = N0
        self.N1 = self.activation(np.dot(self.W1, self.N0) + self.B1)
        self.N2 = self.activation(np.dot(self.W2, self.N1) + self.B2)
        self.N3 = self.activation(np.dot(self.W3, self.N2) + self.B3)

    def suggest(self, state):
        self.evaluate(state.flatten())
        return self.N3.argmax()

    def activation(self, A):
        return 1.0/(1.0 + np.exp(-A))

    def __str__(self):
        s = ''
        s += str(self.W1)
        s += str(self.W2)
        s += str(self.W3)
        s += str(self.B1)
        s += str(self.B2)
        s += str(self.B3)
        return s
