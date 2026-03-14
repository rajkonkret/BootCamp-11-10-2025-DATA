import os
import random

import numpy as np
from tensorflow.python.ops.image_ops_impl import random_hue

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


def print_board(board):
    symbols = {0: " ", 1: "X", -1: "0"}
    print()
    for i in range(3):
        print(" | ".join(symbols[board[3 * i + j]] for j in range(3)))
        if i < 2:
            print("---------")


def check_winner(board):
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        vals = [board[i] for i in combo]
        if all(v == 1 for v in vals): return 1
        if all(v == -1 for v in vals): return -1
    if all(v != 0 for v in board): return 0
    return None


if __name__ == '__main__':
    board = [0] * 9
    # print(print_board(board))
    print("Zaczynamy grę")

    while True:
        print_board(board)
        move = int(input("Podaj swój ruch (0-8): "))
        if not is_valid_move(board, move):
            print("Niepoprawny ruch")
            continue

        board[move] = -1

        winner = check_winner(board)
        if winner is not None:
            break

        prediction = model.predict(np.array([board]), verbose=0)[0]
        posible_moves = get_empty_indicates(board)
        best_move = np.argmax([prediction[i] if i in posible_moves else -1 for i in range(9)])

        board[best_move] = 1

        winner = check_winner(board)
        if winner is not None:
            break

    print_board(board)
    if winner == 1:
        print("AI wygrywa")
    elif winner == -1:
        print("Brawo! Wygrałeś")
    else:
        print("Remis")
