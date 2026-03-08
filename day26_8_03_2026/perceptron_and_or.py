import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# dane wejściowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

y = np.array([
    [0, 0],  # AND, OR
    [0, 1],
    [0, 1],
    [1, 1]
])

np.random.seed(42)

W = np.random.rand(2, 2) * 2 - 1
bias = np.random.rand(2) * 2 - 1

learning_rate = 0.1
epochs = 100

for epoch in range(epochs):
    weighed_sum = np.dot(X, W) + bias
    output = sigmoid(weighed_sum)

    error = y - output

    delta = error * sigmoid_derivative(output)

    # aktualizacja wag i bias
    W += np.dot(X.T, delta) * learning_rate
    bias += np.sum(delta, axis=0) * learning_rate

for i in range(4):
    wynik = sigmoid(np.dot(X[i], W) + bias)
    print(f"Wejście: {X[i]} -> AND: {int(wynik[0] > 0.5)}, OR: {int(wynik[1] > 0.5)}")
# Wejście: [0 0] -> AND: 0, OR: 0
# Wejście: [0 1] -> AND: 0, OR: 1
# Wejście: [1 0] -> AND: 0, OR: 1
# Wejście: [1 1] -> AND: 1, OR: 1
