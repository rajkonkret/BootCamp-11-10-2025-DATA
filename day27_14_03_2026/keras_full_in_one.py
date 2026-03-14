import os
import numpy as np
import time

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # przed importowaniem kerasa

import tensorflow as tf
from tensorflow import keras
from keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("Dostępne urządzenia:", tf.config.list_physical_devices())

# dane wejściowe
X = np.array(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
)

y = np.array(
    [
        [0, 0, 0],  # and, or, xor
        [0, 1, 1],
        [0, 1, 1],
        [1, 1, 0],
    ]
)

# tworzymy model
# 2 wejścia
# 4 neurony warstwa ukryta
# 3 neurony warstwa wyjścia
model = Sequential(
    [
        Input(shape=(2,)),
        Dense(4, activation="relu"),
        Dense(3, activation="sigmoid")
    ]
)

# kompilacja modelu
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])

start_time = time.time()

with tf.device("/GPU:0"):
    model.fit(X, y, epochs=1000, verbose=1)

print(f"Estimated time: {time.time() - start_time}")

# testowanie modelu
predictions = model.predict(X)
predictions = (predictions > 0.5).astype(int)

print("Przewidywane wartości dla AND, OR, XOR\n")
for i in range(len(X)):
    print(f"Wejście {X[i]} => AND: {predictions[i][0]} OR: {predictions[i][1]}, XOR: {predictions[i][2]}")

# zapisanie modelu
model.save("logic_gates.keras")

# zapisanie wag i biasów z modelu numpy
weights = model.get_weights()

filename = "weights_only_full.npz"
np.savez(filename, *weights)
print("Model i wagi zapisane do odpowiednich plików")
# Przewidywane wartości dla AND, OR, XOR
#
# Wejście [0 0] => AND: 0 OR: 0, XOR: 0
# Wejście [0 1] => AND: 0 OR: 1, XOR: 1
# Wejście [1 0] => AND: 0 OR: 1, XOR: 1
# Wejście [1 1] => AND: 1 OR: 1, XOR: 0
# Model i wagi zapisane do odpowiednich plików