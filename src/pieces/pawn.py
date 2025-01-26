from move import Move
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
                possible_moves.append([Move(initial_row=square.row, initial_col=square.col, target_row=new_row, target_col=square.col, piece=self)])

        for i in [-1, 1]:
            new_row = square.row + self.direction
            new_col = square.col + i
            target_square: Square = grid.get_square_by_row_and_col(new_row, new_col)
            if target_square.has_enemy(self.color):
                possible_moves.append([Move(initial_row=square.row, initial_col=square.col, target_row=new_row, target_col=new_col, piece=self)])

        possible_moves.extend(self._get_en_passant_moves(square, grid))

        return possible_moves

    def _get_en_passant_moves(self, square: Square, grid):
        en_passant_moves = []
        
        # Check if the last move was a 2-square pawn move from the opponent
        last_move = grid.get_last_move()
        if last_move:
            last_piece = last_move.piece
            if isinstance(last_piece, Pawn) and last_piece.color != self.color:
                # Check if the opponent's pawn moved two squares forward
                if abs(last_move.initial_row - last_move.target_row) == 2 and square.row == last_move.target_row:
                    # Check if the opponent's pawn is adjacent
                    if abs(square.col - last_move.target_col) == 1:
                        en_passant_target_col = last_move.target_col
                        en_passant_target_row = square.row + self.direction
                        en_passant_moves.append([Move(initial_row=square.row, initial_col=square.col,
                                                      target_row=en_passant_target_row, target_col=en_passant_target_col,
                                                      piece=self, en_passant=True)])

        return en_passant_moves

class BlackPawn(Pawn):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_pawn.png")


class WhitePawn(Pawn):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_pawn.png")
