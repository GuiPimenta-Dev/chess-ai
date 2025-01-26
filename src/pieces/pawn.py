from pieces import Piece

from square import Square


class Pawn(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="Pawn", direction=direction, color=color, asset=asset, value=1
        )

    def _get_possible_moves_in_each_direction(self, square:Square, grid):
        possible_moves = []
        
        steps = 1 if len(self.moves) > 0 else 2
        for i in range(1, steps + 1):
            new_row = square.row + i * self.direction
            target_square: Square = grid.get_square_by_row_and_col(new_row, square.col)
            if target_square.is_empty():
                possible_moves.append([(new_row, square.col)])

        for i in [-1, 1]:
            new_row = square.row + self.direction
            new_col = square.col + i
            target_square: Square = grid.get_square_by_row_and_col(new_row, new_col)
            if target_square.has_enemy(self.color):
                possible_moves.append([(new_row, new_col)])

    
        return possible_moves


class BlackPawn(Pawn):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_pawn.png")


class WhitePawn(Pawn):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_pawn.png")
