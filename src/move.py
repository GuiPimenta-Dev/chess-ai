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

    def __eq__(self, other):
        return self.initial_row == other.initial_row and self.initial_col == other.initial_col and self.target_row == other.target_row and self.target_col == other.target_col and self.piece.id == other.piece.id