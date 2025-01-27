from typing import List
from const import COLS, ROWS
from grid import Grid
from move import Move
from pieces import Piece
from square import Square


class Board:
    def __init__(self, play_as_white=True):
        self.grid = Grid(play_as_white)
        self.turn = "white"
        self.checks = {"white": [], "black": []}
        self.moves = []
        self.possible_moves = self._get_all_possible_moves(self.turn)

    def move(self, row, col, piece):
        moves = []
        
        promotion = []
        for possible_move in self.possible_moves:
            if possible_move.promotion:
                promotion.append(possible_move)
                
        for possible_move in self.possible_moves:
            if (
                possible_move.target_row == row
                and possible_move.target_col == col
                and piece == possible_move.piece
            ):
                moves.append(possible_move)

        if not moves:
            return

        move = moves[0]
        self.grid.move_piece(move)
        self.moves.append(move)
        move.piece.add_move(move)
        self._switch_turn()

    def _get_all_possible_moves(self, color):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                piece: Piece = self.grid.get_square_by_row_and_col(row, col).piece
                if piece and piece.color == color:
                    moves.extend(piece.get_possible_moves(row, col, self.grid))
        
        for move in moves:
            if move.promotion:
                pass
        return moves

    def _switch_turn(self):
        self.turn = "white" if self.turn == "black" else "black"
        white_possible_moves = self.get_possible_moves_by_color("white")
        black_possible_moves = self.get_possible_moves_by_color("black")
        self.possible_moves = white_possible_moves + black_possible_moves

    def get_possible_moves_by_color(self, color):
        is_king_in_check = self.is_king_in_check(color)

        if is_king_in_check:
            return self._get_protective_moves(color)

        safe_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                square = self.grid.get_square_by_row_and_col(row, col)
                if square.has_piece() and square.piece.color == color:
                    piece = square.piece
                    possible_moves = piece.get_possible_moves(row, col, self.grid)

                    for move in possible_moves:
                        # Simulate the move
                        captured_piece = self.grid.get_square_by_row_and_col(
                            move.target_row, move.target_col
                        ).piece
                        initial_square = self.grid.get_square_by_row_and_col(
                            move.initial_row, move.initial_col
                        )
                        target_square = self.grid.get_square_by_row_and_col(
                            move.target_row, move.target_col
                        )

                        target_square.piece = piece
                        initial_square.piece = None

                        if not self.is_king_in_check(color):
                            safe_moves.append(move)

                        # Undo the simulated move
                        initial_square.piece = piece
                        target_square.piece = captured_piece

        return safe_moves

    def _get_protective_moves(self, color):
        protective_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                square = self.grid.get_square_by_row_and_col(row, col)
                if square.has_piece() and square.piece.color == color:
                    piece = square.piece
                    possible_moves = piece.get_possible_moves(row, col, self.grid)
                    for move in possible_moves:
                        captured_piece = self.grid.get_square_by_row_and_col(
                            move.target_row, move.target_col
                        ).piece
                        initial_square = self.grid.get_square_by_row_and_col(
                            move.initial_row, move.initial_col
                        )
                        target_square = self.grid.get_square_by_row_and_col(
                            move.target_row, move.target_col
                        )
                        target_square.piece = piece
                        initial_square.piece = None
                        if not self.is_king_in_check(color):
                            protective_moves.append(move)
                        initial_square.piece = piece
                        target_square.piece = captured_piece
        return protective_moves

    def is_king_in_check(self, color: str) -> bool:
        enemy_color = "black" if color == "white" else "white"
        king_square = self.grid.get_square_by_piece_name_and_color("King", color)
        for move in self._get_all_possible_moves(enemy_color):
            if (
                king_square
                and move.target_row == king_square.row
                and move.target_col == king_square.col
            ):
                return True

        return False

    def get_checks(self, color: str) -> List[Move]:
        checks = []
        enemy_color = "black" if color == "white" else "white"
        king_square = self.grid.get_square_by_piece_name_and_color("King", color)
        for move in self._get_all_possible_moves(enemy_color):
            if (
                move.target_row == king_square.row
                and move.target_col == king_square.col
            ):
                checks.append(move)

        return checks
