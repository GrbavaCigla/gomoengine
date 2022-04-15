#!/usr/bin/python3
from typing import List, Tuple
from sys import argv

from .heuristics import get_rating

BOARD_SIZE = 20


def read_moves(filepath: str) -> Tuple[List[List[int]], int]:
    board = [[0 for _ in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    max_player = 2

    try:
        with open(filepath, "r") as file:
            rows = file.read().splitlines()[1:]
            rows = [i.split() for i in rows]
            rows = [(int(i[0]), int(i[1])) for i in rows]

            for i, (x, y) in enumerate(rows):
                board[x][y] = (i % 2) + 1

    except FileNotFoundError:
        max_player = 1

    return (board, max_player)


def print_board(board):
    for i in board:
        print(i)


def get_next_minmax_move(board, player, alpha, beta, depth=3, is_max=True) -> Tuple[float, int, int]:
    if depth == 0:
        return get_rating(board, player), -1, -1

    best_score, x, y = 0, -1, -1
    if is_max:
        best_score = float("-inf")
    else:
        best_score = float("inf")

    # TODO: Refactor this mess
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                board[i][j] = player
                score, _, _ = get_next_minmax_move(
                    board, player, alpha, beta, depth - 1, not is_max
                )
                board[i][j] = 0

                if is_max and score > best_score or not is_max and score < best_score:
                    x, y = i, j
                    best_score = score
                
                if is_max:
                    if score >= beta:
                        break
                    alpha = max(alpha, score)
                else:
                    if score <= alpha:
                        break
                    beta = min(beta, score)
        else:
            continue
        break
                
    
    return best_score, x, y


if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage: {argv[0]} [filepath of moves.txt]")
        exit(1)

    board, player = read_moves(argv[1])

    score, x, y = get_next_minmax_move(board, player, float("-inf"), float("inf"))

    print(x, y)
