import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist


# funkce aktywacji
def relu(x):
    return np.maximum(x, 0)


def relu_derivative(x):
    return (x > 0).astype(np.float32)


def softmax(x):
    x -= np.max(x, axis=1, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=1, keepdims=True)


# funkcja strat
def cross_entropy(predictions, labels):
    return -np.mean(np.sum(labels * np.log(predictions + 1e-8), axis=1))


# one hot encoding
def one_hot(y, num_classes=10):
    return np.eye(num_classes)[y]


# wczytaj dane
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 784).astype(np.float32) / 255.0
x_test = x_test.reshape(-1, 784).astype(np.float32) / 255.0
y_train_oh = one_hot(y_train)
y_test_oh = one_hot(y_test)

# Inicjalizacja wag
np.random.seed(42)
w1 = np.random.randn(784, 128) * 0.01
b1 = np.zeros((1, 128))
w2 = np.random.randn(128, 10) * 0.01
b2 = np.zeros((1, 10))
