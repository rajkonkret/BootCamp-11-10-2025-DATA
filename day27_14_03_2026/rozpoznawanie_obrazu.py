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

# parametry treningu
lr = 0.1
epochs = 5
batch_size = 64

# trening
for epoch in range(epochs):
    for i in range(0, len(x_train), batch_size):
        x_batch = x_train[i:i + batch_size]
        y_batch = y_train_oh[i:i + batch_size]

        z1 = x_batch @ w1 + b1  # @ odpowiednik dot
        a1 = relu(z1)
        z2 = a1 @ w2 + b2
        y_pred = softmax(z2)

        # loss
        loss = cross_entropy(y_pred, y_batch)

        # backpropagation
        dz2 = y_pred - y_batch
        dw2 = a1.T @ dz2 / batch_size
        db2 = np.sum(dz2, axis=0, keepdims=True) / batch_size

        da1 = dz2 @ w2.T
        dz1 = da1 * relu_derivative(z1)
        dw1 = x_batch.T @ dz1 / batch_size
        db1 = np.sum(dz1, axis=0, keepdims=True) / batch_size

        # aktualizacja wag i bias
        w1 -= lr * dw1
        b1 -= lr * db1
        w2 -= lr * dw2
        b2 -= lr * db2

    print(f"Epoka {epoch + 1}, strata: {loss:.4f}")

# testowanie jedej próbki
idx = 7
x = x_test[idx].reshape(1, -1)
y_true = y_test[idx]

z1 = x @ w1 + b1
a1 = relu(z1)
z2 = a1 @ w2 + b2
y_pred = softmax(z2)

predicted_class = np.argmax(y_pred)

print("Prawdziwa cyfra:", y_true)
print("Sieć przewidziała: ", predicted_class)
print("Poprawnie?", predicted_class == y_true)

plt.imshow(x_test[idx].reshape(28, 28), cmap='gray')
plt.title(f"Prawda: {y_true}, Przewidziano: {predicted_class}")
plt.axis('off')
plt.show()
