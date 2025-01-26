from pieces import Piece


class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece is not None

    def has_ally(self, color):
        return self.piece and self.piece.color == color

    def has_enemy(self, color):
        return self.piece and self.piece.color != color
