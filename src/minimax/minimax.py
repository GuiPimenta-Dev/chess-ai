from typing import Optional
import copy  # Importing the copy module to create deep copies of the board
from tqdm import tqdm  # Importing tqdm for the progress bar

from board import Board
from const import COLS, ROWS
from move import Move

class Minimax:
    def __init__(self, board: Board, max_depth: int = 3):
        self.board = board
        self.max_depth = max_depth

    def evaluate_board(self, board: Board) -> int:
        """
        Evaluate the current board state.
        Positive scores favor white, negative scores favor black.
        """
        score = 0
        for row in range(ROWS):
            for col in range(COLS):
                square = board.grid.get_square_by_row_and_col(row, col)
                if square.has_piece():
                    piece = square.piece
                    score += piece.value if piece.color == "white" else -piece.value
        return score

    def minimax(self, depth: int, maximizing: bool) -> int:
        """
        Recursive minimax algorithm.
        - maximizing: True if it's the maximizing player's turn (e.g., AI's turn).
        """
        if depth == 0 or self.is_game_over():
            return self.evaluate_board(self.board)

        color = "white" if maximizing else "black"
        moves = self.board.get_possible_moves_by_color(color)

        if maximizing:
            max_eval = float('-inf')
            # Wrapping the loop with tqdm to show progress
            for move in tqdm(moves, desc="Maximizing", leave=False):
                # Use a temporary board for the simulation
                temp_board = copy.deepcopy(self.board)
                self.simulate_move(temp_board, move)
                eval = self.minimax_with_board(temp_board, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            # Wrapping the loop with tqdm to show progress
            for move in tqdm(moves, desc="Minimizing", leave=False):
                # Use a temporary board for the simulation
                temp_board = copy.deepcopy(self.board)
                self.simulate_move(temp_board, move)
                eval = self.minimax_with_board(temp_board, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self, color: str):
        """
        Find the best move for the given color using the minimax algorithm.
        """
        best_move = None
        best_value = float('-inf') if color == "white" else float('inf')

        moves = self.board.get_possible_moves_by_color(color)
        # Wrapping the loop with tqdm to show progress
        for move in tqdm(moves, desc="Evaluating moves", leave=False):
            # Use a temporary board for the simulation
            temp_board = copy.deepcopy(self.board)
            self.simulate_move(temp_board, move)
            eval = self.minimax_with_board(temp_board, self.max_depth - 1, color == "black")

            if (color == "white" and eval > best_value) or (color == "black" and eval < best_value):
                best_value = eval
                best_move = move

        return best_move

    def minimax_with_board(self, board: Board, depth: int, maximizing: bool) -> int:
        """
        A helper function to use a given board state for minimax evaluation.
        """
        if depth == 0 or self.is_game_over():
            return self.evaluate_board(board)

        color = "white" if maximizing else "black"
        moves = board.get_possible_moves_by_color(color)

        if maximizing:
            max_eval = float('-inf')
            # Wrapping the loop with tqdm to show progress
            for move in tqdm(moves, desc="Maximizing", leave=False):
                temp_board = copy.deepcopy(board)
                self.simulate_move(temp_board, move)
                eval = self.minimax_with_board(temp_board, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            # Wrapping the loop with tqdm to show progress
            for move in tqdm(moves, desc="Minimizing", leave=False):
                temp_board = copy.deepcopy(board)
                self.simulate_move(temp_board, move)
                eval = self.minimax_with_board(temp_board, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def simulate_move(self, board: Board, move: Move):
        """
        Simulate a move on a given board.
        """
        board.grid.move_piece(move)
        board.moves.append(move)
        move.piece.add_move(move)

    def is_game_over(self) -> bool:
        """
        Check if the game is over (e.g., one of the kings is in checkmate).
        """
        white_moves = self.board.get_possible_moves_by_color("white")
        black_moves = self.board.get_possible_moves_by_color("black")
        return not white_moves or not black_moves