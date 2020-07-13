import numpy as np
import random

def Sigmoid(X):
    return 1/(1 + np.exp(-X))

class AgentANN:
    def __init__(self, resolution, child=False):
        if child:
            self.hidden1_weights = np.zeros((3, 8))
            self.hidden2_weights = np.zeros((8, 4))
            self.output_weights = np.zeros((4, 1))
        else:
            self.hidden1_weights = np.random.randn(3, 8)
            self.hidden2_weights = np.random.randn(8, 4)
            self.output_weights = np.random.randn(4, 1)

    def decide(self, screen):
        hidden1_output = Sigmoid(np.dot(screen, self.hidden1_weights))
        hidden2_output = Sigmoid(np.dot(hidden1_output, self.hidden2_weights))
        output = Sigmoid(np.dot(hidden2_output, self.output_weights))
        return round(output[0])


