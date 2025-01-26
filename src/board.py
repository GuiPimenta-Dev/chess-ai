from typing import List
from const import COLS, ROWS
from move import Move
from pieces import Direction
from pieces.bishop import BlackBishop, WhiteBishop
from pieces.king import BlackKing, WhiteKing
from pieces.knight import BlackKnight, WhiteKnight
from pieces.pawn import BlackPawn, WhitePawn
from pieces.queen import BlackQueen, WhiteQueen
from pieces.rook import BlackRook, WhiteRook
from square import Square


class Board:
    def __init__(self, play_as_white=True):
        self.squares = [[None for _ in range(COLS)] for _ in range(COLS)]
        self._create()
        self._add_pieces(play_as_white)

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, play_as_white):

        if play_as_white:
            white_pawns = [WhitePawn(i, direction=Direction.UP) for i in range(1, 9)]
            white_rooks = [WhiteRook(i, direction=Direction.UP) for i in range(1, 3)]
            white_knights = [
                WhiteKnight(i, direction=Direction.UP) for i in range(1, 3)
            ]
            white_bishops = [
                WhiteBishop(i, direction=Direction.UP) for i in range(1, 3)
            ]
            white_queen = WhiteQueen(id=1, direction=Direction.UP)
            white_king = WhiteKing(id=1, direction=Direction.UP)

            black_rooks = [BlackRook(i, direction=Direction.DOWN) for i in range(1, 3)]
            black_pawns = [BlackPawn(i, direction=Direction.DOWN) for i in range(1, 9)]
            black_knights = [
                BlackKnight(i, direction=Direction.DOWN) for i in range(1, 3)
            ]
            black_bishops = [
                BlackBishop(i, direction=Direction.DOWN) for i in range(1, 3)
            ]
            black_queen = BlackQueen(id=1, direction=Direction.DOWN)
            black_king = BlackKing(id=1, direction=Direction.DOWN)

            for i in range(ROWS):
                self.squares[1][i].piece = black_pawns[i]
                self.squares[6][i].piece = white_pawns[i]

            self.squares[0][0].piece = black_rooks[0]
            self.squares[0][7].piece = black_rooks[1]
            self.squares[7][0].piece = white_rooks[0]
            self.squares[7][7].piece = white_rooks[1]
            self.squares[0][1].piece = black_knights[0]
            self.squares[0][6].piece = black_knights[1]
            self.squares[7][1].piece = white_knights[0]
            self.squares[7][6].piece = white_knights[1]
            self.squares[0][2].piece = black_bishops[0]
            self.squares[0][5].piece = black_bishops[1]
            self.squares[7][2].piece = white_bishops[0]
            self.squares[7][5].piece = white_bishops[1]
            self.squares[0][3].piece = black_queen
            self.squares[7][3].piece = white_queen
            self.squares[0][4].piece = black_king
            self.squares[7][4].piece = white_king

        else:

            white_pawns = [WhitePawn(i, direction=Direction.DOWN) for i in range(1, 9)]
            white_rooks = [WhiteRook(i, direction=Direction.DOWN) for i in range(1, 3)]
            white_knights = [
                WhiteKnight(i, direction=Direction.DOWN) for i in range(1, 3)
            ]
            white_bishops = [
                WhiteBishop(i, direction=Direction.DOWN) for i in range(1, 3)
            ]
            white_queen = WhiteQueen(id=1, direction=Direction.DOWN)
            white_king = WhiteKing(id=1, direction=Direction.DOWN)

            black_rooks = [BlackRook(i, direction=Direction.UP) for i in range(1, 3)]
            black_pawns = [BlackPawn(i, direction=Direction.UP) for i in range(1, 9)]
            black_knights = [
                BlackKnight(i, direction=Direction.UP) for i in range(1, 3)
            ]
            black_bishops = [
                BlackBishop(i, direction=Direction.UP) for i in range(1, 3)
            ]
            black_queen = BlackQueen(id=1, direction=Direction.UP)
            black_king = BlackKing(id=1, direction=Direction.UP)

            for i in range(ROWS):
                self.squares[1][i].piece = white_pawns[i]
                self.squares[6][i].piece = black_pawns[i]

            self.squares[0][0].piece = white_rooks[0]
            self.squares[0][7].piece = white_rooks[1]
            self.squares[7][0].piece = black_rooks[0]
            self.squares[7][7].piece = black_rooks[1]
            self.squares[0][1].piece = white_knights[0]
            self.squares[0][6].piece = white_knights[1]
            self.squares[7][1].piece = black_knights[0]
            self.squares[7][6].piece = black_knights[1]
            self.squares[0][2].piece = white_bishops[0]
            self.squares[0][5].piece = white_bishops[1]
            self.squares[7][2].piece = black_bishops[0]
            self.squares[7][5].piece = black_bishops[1]
            self.squares[0][4].piece = white_queen
            self.squares[7][4].piece = black_queen
            self.squares[0][3].piece = white_king
            self.squares[7][3].piece = black_king

    def move(self, possible_moves: List[Move], move: Move):
        if move not in possible_moves:
            return

        self.squares[move.target_row][move.target_col].piece = move.piece
        self.squares[move.initial_row][move.initial_col].piece = None
        move.piece.moved = True

    
    def find_square_of_piece(self, name, color):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.squares[row][col]
                if square.has_piece() and square.piece.name == name and square.piece.color == color:
                    return square
            return None