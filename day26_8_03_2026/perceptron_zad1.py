# perceptron - matematyczne odzwierciedlenie neuronu
# przyjmuje zestaw danych
# suma ważona z = x * w + b
# na podstawie danych wejściowych ustala wagi i dodakowe przesunięcia
# funkcja aktywacji - funkcja która daje wynik działania perceptronu
# np funkcja skokowa wartości 0 lub 1
# perceptron binarny

import numpy as np
import matplotlib.pyplot as plt


class Perceptron:

    def __init__(self, learnig_rate=0.1, epochs=10):
        self.learning_rate = learnig_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def activation_function(self, x):
        return 1 if x >= 0 else 0  # funkcja skokowa

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            for i in range(n_samples):
                linear_output = np.dot(X[i], self.weights) + self.bias
                y_predicted = self.activation_function(linear_output)

                update = self.learning_rate * (y[i] - y_predicted)
                self.weights += update * X[i]
                self.bias += update

    def predict(self, X):
        print(self.weights)
        print(self.bias)

        linear_output = np.dot(X, self.weights) + self.bias
        return np.array([self.activation_function(x) for x in linear_output])

    def set_fit(self):
        self.weights = np.array([0.02, 0.01])
        self.bias = -0.03


def plot_decision_boundary(X, y, model):
    x_min, x_max = -0.5, 1.5
    y_min, y_max = -0.5, 1.5

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)
    plt.scatter(X[:0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
    plt.title("Podział obszaru decyzyjnego")
    plt.xlabel("X1")
    plt.ylabel("X2")

    plt.show()


# AND
# 0 and 0 = 0
# 0 and 1 = 0
# 1 and 0 = 0
# 1 and 1 = 1

# dane trenigowa
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

# perceptron
p = Perceptron(learnig_rate=0.1, epochs=10)

# nauka perceptronu
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki:", predictions)
# [0.2 0.1]
# -0.20000000000000004
# Przewidywane wyniki: [0 0 0 1]

# perceptron
p = Perceptron(learnig_rate=0.01, epochs=3)

# nauka perceptronu
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki:", predictions)
# [0.02 0.01]
# -0.019999999999999997
# Przewidywane wyniki: [0 0 1 1] błedne dane

# perceptron
p = Perceptron(learnig_rate=0.01, epochs=10)

# nauka perceptronu
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki:", predictions)
# [0.02 0.01]
# -0.03
# Przewidywane wyniki: [0 0 0 1]
