import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# dane
# liczba końćzyn, sierść, pióra, waga, ogon
X = np.array([
    [4, 1, 0, 4, 1],  # kot
    [4, 1, 0, 20, 1],  # pies
    [2, 0, 1, 1.5, 0],  # kura
    [4, 1, 0, 5, 1],  # kot
    [4, 1, 0, 25, 1],  # pies
    [2, 0, 1, 2, 0],  # kura
])

y = np.array([
    [1, 0, 0],  # kot
    [0, 1, 0],  # pies
    [0, 0, 1],  # kura
    [1, 0, 0],  # kot
    [0, 1, 0],  # pies
    [0, 0, 1],  # kura
])
