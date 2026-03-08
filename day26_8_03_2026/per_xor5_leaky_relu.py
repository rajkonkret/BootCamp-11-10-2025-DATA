import numpy as np
from sympy.abc import alpha


# Leaky ReLU - funkcja aktywacji - pomaga ominąc problem martwych neuronów
# jest narażone na martwe neurony
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)


# pochodna leaky_relu
def leaky_relu_deriavative(x, alpha=0.01):
    return np.where(x > 0, 1, alpha)


# dane trenigowa XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(42)

# W_hidden = np.random.rand(2, 2) * 2 - 1
# W_output = np.random.rand(2, 2) * 2 - 1

# inicjalizacja wg Xavier/Glorot
W_hidden = np.random.rand(2, 2) * np.sqrt(2 / 2)
W_output = np.random.rand(2, 1) * np.sqrt(2 / 2)

learning_rate = 0.1
epochs = 5000

for epoch in range(epochs):
    # warstwa ukryta
    hidden_input = np.dot(X, W_hidden)
    hidden_output = leaky_relu(hidden_input)

    # warstwa wyjściowa
    final_input = np.dot(hidden_output, W_output)
    final_output = leaky_relu(final_input)

    # bład
    error = y - final_output

    # aktualizacja wag, backpropagation
    d_output = error * leaky_relu_deriavative(final_output)
    error_hidden = d_output.dot(W_output.T)
    d_hidden = error_hidden * leaky_relu_deriavative(hidden_output)

    # aktualizacja wag
    W_output += hidden_output.T.dot(d_output) * learning_rate
    W_hidden += X.T.dot(d_hidden) * learning_rate

# testowanie XOR
for i in range(4):
    # warstwa ukryta
    hidden_input = np.dot(X[i], W_hidden)
    hidden_output = leaky_relu(hidden_input)

    # warstwa wyjściowa
    output_input = np.dot(hidden_output, W_output)
    output = leaky_relu(output_input)

    print(f"Wejście: {X[i]} -> Przewidywane wyjścia: {output[0]:.4f}")
