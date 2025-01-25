from const import COLS, ROWS
from pieces import Piece


class Knight(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="Knight", direction=direction, color=color, asset=asset, value=3
        )

    def possible_moves(self, row, col):
        possible_moves = []
        moves = [
            (-2, -1),
            (-2, 1),
            (2, -1),
            (2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
        ]

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                possible_moves.append([(new_row, new_col)])

        return possible_moves


class BlackKnight(Knight):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_knight.png")


class WhiteKnight(Knight):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_knight.png")
