from typing import List
from const import COLS, ROWS
from grid import Grid
from move import Move
from pieces import Piece


class Board:
    def __init__(self, play_as_white=True):
        self.grid = Grid(play_as_white)
        self.turn = "white"
        self.moves = []
        self.possible_moves = self.get_all_possible_moves(self.turn)

    def move(self, row, col, piece):
        move = None
        for possible_move in self.possible_moves:
            if possible_move.target_row == row and possible_move.target_col == col and piece == possible_move.piece:
                move = possible_move
                break
        
        if not move:
            return

        self.grid.move_piece(move)
        self.moves.append(move)
        move.piece.add_move(move)
        self._switch_turn()

    def is_king_in_check(self, color):
        king = self.grid.get_square_by_piece_name_and_color("King", color).piece
        enemy_color = "black" if color == "white" else "white"
        enemy_possible_moves = self.get_all_possible_moves(enemy_color)
        return king.is_in_check(enemy_possible_moves, self.grid)
        
    def get_all_possible_moves(self, color):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                piece: Piece = self.grid.get_square_by_row_and_col(row, col).piece
                if piece and piece.color == color:
                    moves.extend(piece.get_possible_moves(row, col, self.grid))
        return moves

    def _switch_turn(self):
        self.turn = "white" if self.turn == "black" else "black"
        self.possible_moves = self.get_all_possible_moves(self.turn)
    
    