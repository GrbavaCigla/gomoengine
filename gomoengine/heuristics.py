from itertools import groupby
from typing import List

from .constants import PENALTY


def transpose(board) -> List[List[int]]:
    return [list(i) for i in zip(*board)]


def shift(board) -> List[List[int]]:
    return [padding(r) + row + padding(len(row) - r - 1) for r, row in enumerate(board)]


def padding(n) -> List[int]:
    return [0 for _ in range(n)]


def get_rating(board, player, penalty=PENALTY) -> float:
    score = 0

    for i in (
        board
        + transpose(board)
        + transpose(shift(board))
        + transpose(shift(reversed(board)))
    ):
        groups = [(i, len(list(j))) for i, j in groupby(i)]
        groups = [(0, 1)] + groups + [(0, 1)]
        for i in range(1, len(groups) - 1):
            cur_player, length = groups[i]

            if cur_player == 3 - player and length > 4:
                return float("-inf")
            
            if cur_player == player and length > 4:
                return float("inf")

            if cur_player > 0 and length > 1:
                if groups[i - 1][0] == 0:
                    score += 10 ** length * ((cur_player == player) * (2 + penalty) - 1 - penalty)
                
                if groups[i + 1][0] == 0:
                    score += 10 ** length * ((cur_player == player) * (2 + penalty) - 1 - penalty)
            
    return score
