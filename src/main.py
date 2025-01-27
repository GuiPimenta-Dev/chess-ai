import copy
import time
import pygame
import sys

from const import COLS, ROWS, WIDTH, HEIGHT, SQUARE_SIZE
from game import Game
from minimax.minimax import Minimax


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.play_as_white = True
        self.game = Game(play_as_white=self.play_as_white)
        self.board = self.game.board
        self.grid = self.board.grid
        self.dragger = self.game.dragger
        self.minimax = Minimax(self.board, max_depth=1)  # Initialize Minimax
        self.round = 1
        self.best_move = None

        
    def ai_move(self):
        """
        Use the Minimax algorithm to calculate and execute the best move for the AI.
        """
        color = "white" if self.play_as_white else "black"
        self.best_move = self.minimax.find_best_move(color)
        if self.best_move:
            self.game.show_ai_best_move(self.screen, self.best_move)
        

    def run(self):
        while True:
            self.game.show_bg(self.screen)
            self.game.show_hover(self.screen)
            self.game.show_last_move(self.screen)
            self.game.show_check(self.screen)
            self.game.show_ai_best_move(self.screen, self.best_move)
            self.game.show_pieces(self.screen)
            self.game.show_possible_moves(self.screen)


            if self.dragger.dragging:
                self.dragger.update_blit(self.screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    clicked_row = mouse_y // SQUARE_SIZE
                    clicked_col = mouse_x // SQUARE_SIZE
                    square = self.grid.get_square_by_row_and_col(
                        clicked_row, clicked_col
                    )
                    if not square.has_piece() or square.piece.color != self.board.turn:
                        continue

                    self.dragger.update_mouse(event.pos)
                    self.dragger.save_initial(event.pos)
                    self.dragger.drag_piece(square.piece)

                elif event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    clicked_row = mouse_y // SQUARE_SIZE
                    clicked_col = mouse_x // SQUARE_SIZE

                    if (
                        clicked_col < 0
                        or clicked_col >= COLS
                        or clicked_row < 0
                        or clicked_row >= ROWS
                    ):
                        continue

                    self.game.set_hover(clicked_row, clicked_col)

                    if self.dragger.dragging:
                        self.dragger.update_mouse(event.pos)
                        self.game.show_bg(self.screen)
                        self.game.show_hover(self.screen)
                        self.game.show_last_move(self.screen)
                        self.game.show_check(self.screen)
                        self.game.show_ai_best_move(self.screen, self.best_move)
                        self.game.show_pieces(self.screen)
                        self.game.show_possible_moves(self.screen)
                        self.dragger.update_blit(self.screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.dragger.update_mouse(event.pos)
                    clicked_row = self.dragger.mouse_y // SQUARE_SIZE
                    clicked_col = self.dragger.mouse_x // SQUARE_SIZE
                    self.board.move(clicked_row, clicked_col, self.dragger.piece)
                    self.dragger.undrag_piece()

                    # Trigger AI's turn after the player moves
                    ai_color = "white" if self.play_as_white else "black"
                    if ai_color == self.board.turn:
                        self.round += 1
                    if not self.board.is_game_over() and self.round > 4 and self.board.turn == ai_color:
                        self.ai_move()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    Main().run()