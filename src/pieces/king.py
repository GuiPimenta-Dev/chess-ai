from const import COLS, ROWS
from pieces import Piece


class King(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="King", direction=direction, color=color, asset=asset
        )

    def _get_possible_moves_in_each_direction(self, square, _):
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
            new_row = square.row + dr
            new_col = square.col + dc
            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                possible_moves.append([(new_row, new_col)])

        return possible_moves


class BlackKing(King):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_king.png")


class WhiteKing(King):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_king.png")
