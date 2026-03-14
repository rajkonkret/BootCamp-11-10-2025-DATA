import os
import random

import numpy as np

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # przed importowaniem kerasa

import tensorflow as tf
from tensorflow import keras
from keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

X = []
y = []


def is_valid_move(board, move):
    return board[move] == 0


def get_empty_indicates(board):
    return [i for i, val in enumerate(board) if val == 0]


# losowanie danych do nauki
for _ in range(5000):
    board = [0] * 9
    moves = random.randint(1, 5)

    for _ in range(moves):
        empty = get_empty_indicates(board)
        if not empty:
            break
        move = random.choice(empty)
        board[move] = random.choice([-1, 1])

    empty = get_empty_indicates(board)
    if empty:
        target_move = random.choice(empty)
        X.append(board)
        y.append(target_move)

X = np.array(X)
y = tf.keras.utils.to_categorical(y, num_classes=9)

model = Sequential(
    [
        Input(shape=(9,)),
        Dense(64, activation="relu"),
        Dense(64, activation="relu"),
        Dense(9, activation="softmax"),
    ]
)

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])
model.fit(X, y, epochs=20, batch_size=32, verbose=2)

