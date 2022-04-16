from typing import List, Tuple
BOARD_SIZE = 20


def is_near(board, x, y) -> bool:
    for i in range(3):
        for j in range(3):
            try:
                if i == 1 and j == 1:
                    continue
                if x + i < 1 or y + j < 1:
                    continue

                if board[x + i - 1][y + j - 1] != 0:
                    return True

            except IndexError:
                pass
    
    return False
