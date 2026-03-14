import os
import math

# plansza
board = [" " for _ in range(9)]


def print_board(board):
    symbols = {0: " ", 1: "X", -1: "0"}
    os.system("clear")  # macOs/Linux (użyj cls dla Windows)
    print("Aktualna plansza")
    print()
    for i, row in enumerate([board[i * 3:(i + 3) * 3] for i in range(3)]):
        print(" | ".join(cell if cell != " " else str(i * 3 + j) for j, cell in enumerate(row)))
        if i < 2:
            print("--+---+--")

    print()


def check_winner(b, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        if all(b[i] == player for i in combo):
            return True
    return False
