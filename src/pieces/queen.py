from const import COLS, ROWS
from pieces import Piece


class Queen(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="Queen", direction=direction, color=color, asset=asset, value=9
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
            directional_moves = []
            for i in range(1, COLS):
                new_row = row + i * dr
                new_col = col + i * dc
                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    directional_moves.append((new_row, new_col))
                else:
                    break

            if directional_moves:
                possible_moves.append(directional_moves)

        return possible_moves


class BlackQueen(Queen):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_queen.png")


class WhiteQueen(Queen):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_queen.png")
