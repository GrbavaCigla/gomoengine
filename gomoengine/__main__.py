#!/usr/bin/python3
from typing import List, Tuple
from sys import argv

from .heuristics import get_rating
from .minimax import get_minimax_move
from . import BOARD_SIZE


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

            max_player = len(rows) % 2 + 1

    except FileNotFoundError:
        max_player = 1

    return (board, max_player)


def board_to_str(board) -> str:
    return "\n".join([" ".join([str(j) for j in i]) for i in board])


if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage: {argv[0]} [filepath of moves.txt]")
        exit(1)

    board, player = read_moves(argv[1])

    score, x, y = get_minimax_move(board, player, float("-inf"), float("inf"))

    # board[x][y] = player
    with open("bla.log", "w+") as file:
        file.write(f"{score} {player}\n\n{board_to_str(board)}")

    print(x, y)
