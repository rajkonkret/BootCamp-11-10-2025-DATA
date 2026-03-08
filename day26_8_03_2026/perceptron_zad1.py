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
        self.weights = np.array([0.2, 0.1])
        self.bias = 0.2
