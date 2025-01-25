from pieces import Piece


class Move:
    def __init__(
        self,
        initial_row,
        initial_col,
        target_row,
        target_col,
        piece: Piece,
        captured_piece: Piece = None,
        promotion=None,
    ):
        self.initial_row = initial_row
        self.initial_col = initial_col
        self.target_row = target_row
        self.target_col = target_col
        self.piece = piece
        self.captured_piece = captured_piece
        self.promotion = promotion

    def __repr__(self):
        return f"({self.row}, {self.col})"
