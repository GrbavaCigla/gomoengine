from itertools import groupby
from typing import List


def transpose(board) -> List[List[int]]:
    return [list(i) for i in zip(*board)]


def shift(board) -> List[List[int]]:
    return [padding(r) + row + padding(len(row) - r - 1) for r, row in enumerate(board)]


def padding(n) -> List[int]:
    return [0 for _ in range(n)]


def get_rating(board, player) -> int:
    score = 0

    for i in (
        board
        + transpose(board)
        + transpose(shift(board))
        + transpose(shift(reversed(board)))
    ):
        for pl, cel in groupby(i):
            cel = list(cel)
            if pl == player and len(cel) > 1:
                score += 10 ** len(cel)
            if pl == 3 - player and len(cel) > 1:
                score -= 10 ** len(cel)

    return score
