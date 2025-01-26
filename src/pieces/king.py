from const import COLS, ROWS
from pieces import Piece


class King(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="King", direction=direction, color=color, asset=asset
        )
        self.checks = []
        

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
    
    def is_in_check(self, enemy_possible_moves, grid):
        is_in_check = False
        king_square = grid.get_square_by_piece_name_and_color("King", self.color)
        for move in enemy_possible_moves:
            if move.target_row == king_square.row and move.target_col == king_square.col:
                is_in_check = True
                self.checks.append(move)
        return is_in_check
    
class BlackKing(King):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_king.png")


class WhiteKing(King):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_king.png")
