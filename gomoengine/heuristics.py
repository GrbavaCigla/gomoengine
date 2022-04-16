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
        groups = [(i, len(list(j))) for i, j in groupby(i)]
        groups = [(0, 1)] + groups + [(0, 1)]
        # TODO: Prioritize 4 in a row
        for i in range(1, len(groups) - 1):
            cur_player, length = groups[i]

            if cur_player > 0:
                if groups[i - 1][0] == 0 and length > 1:
                    score += 10 ** length * ((cur_player == player) * 2 - 1)
                
                if groups[i + 1][0] == 0 and length > 1:
                    score += 10 ** length * ((cur_player == player) * 2 - 1)
            
    return score
