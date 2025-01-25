from const import COLS, ROWS
from pieces import Piece


class Bishop(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="Bishop", direction=direction, color=color, asset=asset, value=3
        )

    def possible_moves(self, row, col):
        possible_moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            direction_moves = []
            for i in range(1, 8):
                new_row = row + i * dr
                new_col = col + i * dc
                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    direction_moves.append((new_row, new_col))
                else:
                    break
            possible_moves.append(direction_moves)

        return possible_moves


class BlackBishop(Bishop):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_bishop.png")


class WhiteBishop(Bishop):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_bishop.png")
