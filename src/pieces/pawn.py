from const import COLS, ROWS
from pieces import Piece
from typing import override


class Pawn(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="Pawn", direction=direction, color=color, asset=asset, value=1
        )

    def possible_moves(self, row, col):
        possible_moves = []
        steps = 1 if self.moved else 2
        for i in range(1, steps + 1):
            new_row = row + i * self.direction
            if 0 <= new_row < ROWS:
                possible_moves.append([(new_row, col)])

        return possible_moves

    def possible_attacks(self, row, col):
        possible_moves = []
        for i in [-1, 1]:
            new_row = row + self.direction
            new_col = col + i
            possible_moves.append([(new_row, new_col)])
        return possible_moves


class BlackPawn(Pawn):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_pawn.png")


class WhitePawn(Pawn):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_pawn.png")
