#!/usr/bin/python3
from typing import List, Tuple
from os import path
from random import randint

from heuristics import get_rating

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


def write_move(filepath, x, y):
    with open(filepath, "w+") as file:
        file.write(f"{x} {y}")


def set_rand_move(board: List[List[int]]) -> Tuple[int, int]:
    num_empty = sum([i.count(0) for i in board])

    if num_empty == 0:
        return (-1, -1)

    num = randint(0, num_empty)

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                if not num:
                    return (i, j)
                num -= 1

    return (-1, -1)


def print_board(board):
    for i in board:
        print(i)


def get_next_minmax_move(board, player, alpha, beta, depth=1, is_max=True) -> Tuple[int, int, int]:
    if depth == 0:
        return get_rating(board, player), -1, -1

    best_score, x, y = 0, -1, -1
    if is_max:
        best_score = float("-inf")
    else:
        best_score = float("inf")

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                board[i][j] = player
                score, _, _ = get_next_minmax_move(board, player, depth - 1, not is_max)
                board[i][j] = 0

                if is_max and score > best_score or not is_max and score < best_score:
                    x, y = i, j
                    best_score = score

    return int(best_score), x, y


if __name__ == "__main__":
    moves_path = path.join(path.dirname(__file__), "moves.txt")
    play_path = path.join(path.dirname(__file__), "play.txt")

    board, player = read_moves(moves_path)

    print_board(board)

    # x, y = set_rand_move(board)
    score, x, y = get_next_minmax_move(board, player)

    write_move(play_path, x, y)
