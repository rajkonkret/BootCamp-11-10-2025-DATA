# perceptron wielowarstwowy

# warstwa wejściowa
# warstwa ukryta
# warstwa wyjściowa

# Optuna/KersTuner
import numpy as np


# funkcja aktywacji, sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# dane trenigowa XOR
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# y = np.array([[0], [1], [1], [0]])

# AND
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])
np.random.seed(42)

W_hidden = np.random.rand(2, 2)
W_output = np.random.rand(2, 1)

learning_rate = 0.5
epochs = 5000

for epoch in range(epochs):
    # warstwa ukryta
    hidden_input = np.dot(X, W_hidden)
    hidden_output = sigmoid(hidden_input)

    # warstwa wyjściowa
    output_input = np.dot(hidden_output, W_output)
    output = sigmoid(output_input)

    # bład
    error = y - output

    # aktualizacja wag, backpropagation
    d_output = error * (output * (1 - output))
    error_hidden = d_output.dot(W_output.T)
    d_hidden = error_hidden * (hidden_output * (1 - hidden_output))

    # aktualizacja wag
    W_output += hidden_output.T.dot(d_output) * learning_rate
    W_hidden += X.T.dot(d_hidden) * learning_rate

# testowanie XOR
for i in range(4):
    # warstwa ukryta
    hidden_input = np.dot(X[i], W_hidden)
    hidden_output = sigmoid(hidden_input)

    # warstwa wyjściowa
    output_input = np.dot(hidden_output, W_output)
    output = sigmoid(output_input)

    print(f"Wejście: {X[i]} -> Przewidywane wyjścia: {output[0]:.4f}")
# Wejście: [0 0] -> Przewidywane wyjścia: 0.0943
# Wejście: [0 1] -> Przewidywane wyjścia: 0.8466
# Wejście: [1 0] -> Przewidywane wyjścia: 0.8466
# Wejście: [1 1] -> Przewidywane wyjścia: 0.2026

# AND
# Wejście: [0 0] -> Przewidywane wyjścia: 0.0026
# Wejście: [0 1] -> Przewidywane wyjścia: 0.0214
# Wejście: [1 0] -> Przewidywane wyjścia: 0.0244
# Wejście: [1 1] -> Przewidywane wyjścia: 0.4976
