import numpy as np


def xor(a, b):
    return int(a != b)


print(xor(0, 0))  # 0
print(xor(0, 1))  # 1
print(xor(1, 0))  # 1
print(xor(1, 1))  # 0


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


# dane trenigowa
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# perceptron
p = Perceptron(learnig_rate=0.1, epochs=10)

# nauka perceptronu
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki:", predictions)
#   [-0.1  0. ]
# 0.0
# Przewidywane wyniki: [1 1 0 0]

# dłusza nauka
# perceptron
p = Perceptron(learnig_rate=0.1, epochs=500)

# nauka perceptronu
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki:", predictions)
# [-0.1  0. ]
# 0.0
# Przewidywane wyniki: [1 1 0 0]
