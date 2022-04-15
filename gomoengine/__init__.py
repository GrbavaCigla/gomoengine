from typing import Tuple
from .heuristics import get_rating

BOARD_SIZE = 20


def get_next_minimax_move(
    board, player, alpha, beta, depth=3, is_max=True
) -> Tuple[float, int, int]:
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
                score, _, _ = get_next_minimax_move(
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
