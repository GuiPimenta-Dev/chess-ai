from const import COLS, ROWS
from pieces import Piece


class King(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="King", direction=direction, color=color, asset=asset
        )

    def possible_moves(self, row, col):
        possible_moves = []
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                possible_moves.append([(new_row, new_col)])

        return possible_moves


class BlackKing(King):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_king.png")


class WhiteKing(King):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_king.png")
