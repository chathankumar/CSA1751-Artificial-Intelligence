import random
import math

# Activation functions and their derivatives
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def relu(x):
    return max(0, x)

def relu_derivative(x):
    return 1 if x > 0 else 0

# Helper function to initialize weights
def initialize_weights(rows, cols):
    return [[random.uniform(-1, 1) for _ in range(cols)] for _ in range(rows)]

# Helper function to calculate dot product
def dot_product(vec1, vec2):
    return sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases randomly
        self.weights1 = initialize_weights(input_size, hidden_size)
        self.bias1 = [0 for _ in range(hidden_size)]
        self.weights2 = initialize_weights(hidden_size, output_size)
        self.bias2 = [0 for _ in range(output_size)]

    def forward(self, X):
        # Forward propagation
        self.z1 = [dot_product(X, self.weights1[j]) + self.bias1[j] for j in range(len(self.bias1))]
        self.a1 = [relu(z) for z in self.z1]

        self.z2 = [dot_product(self.a1, self.weights2[j]) + self.bias2[j] for j in range(len(self.bias2))]
        self.a2 = [sigmoid(z) for z in self.z2]
        return self.a2

    def backward(self, X, y, output, learning_rate):
        # Output layer error
        output_error = [(output[i] - y[i]) for i in range(len(y))]
        output_delta = [output_error[i] * sigmoid_derivative(output[i]) for i in range(len(output))]

        # Hidden layer error
        a1_error = [dot_product(output_delta, [self.weights2[j][i] for j in range(len(self.weights2))]) for i in range(len(self.a1))]
        a1_delta = [a1_error[i] * relu_derivative(self.z1[i]) for i in range(len(self.a1))]

        # Update weights and biases (for output layer)
        for i in range(len(self.weights2)):
            for j in range(len(self.weights2[i])):
                self.weights2[i][j] -= learning_rate * self.a1[j] * output_delta[i]
            self.bias2[i] -= learning_rate * output_delta[i]

        # Update weights and biases (for hidden layer)
        for i in range(len(self.weights1)):
            for j in range(len(self.weights1[i])):
                self.weights1[i][j] -= learning_rate * X[j] * a1_delta[i]
            self.bias1[i] -= learning_rate * a1_delta[i]

    def train(self, X, y, epochs, learning_rate):
        for _ in range(epochs):
            for i in range(len(X)):
                output = self.forward(X[i])
                self.backward(X[i], y[i], output, learning_rate)

# Example usage:
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]  # XOR problem

nn = FeedForwardNN(2, 2, 1)  # 2 inputs, 2 hidden neurons, 1 output
nn.train(X, y, epochs=10000, learning_rate=0.1)

for i in range(len(X)):
    print(f"Input: {X[i]} => Output: {nn.forward(X[i])}")
