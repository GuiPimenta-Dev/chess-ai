import pygame
import sys

from const import WIDTH, HEIGHT, SQUARE_SIZE
from game import Game

class Main:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    self.game = Game(play_as_white=False)
    self.board = self.game.board
    self.dragger = self.game.dragger
  
  def run(self):
    while True:
      self.game.show_bg(self.screen)
      self.game.show_pieces(self.screen)
      self.game.show_possible_moves(self.screen)
      
      if self.dragger.dragging:
        self.dragger.update_blit(self.screen)
      
      for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_x, mouse_y = event.pos
          clicked_row = mouse_y // SQUARE_SIZE
          clicked_col = mouse_x // SQUARE_SIZE
          square = self.board.squares[clicked_row][clicked_col]
          if square.has_piece() and square.piece.color != self.game.turn:
            continue
          
          self.dragger.update_mouse(event.pos)
          self.game.set_possible_moves(clicked_row, clicked_col)
          
          self.dragger.save_initial(event.pos)
          self.dragger.drag_piece(square.piece)
        
        elif event.type == pygame.MOUSEMOTION:
          if self.dragger.dragging:
            self.dragger.update_mouse(event.pos)
            self.game.show_bg(self.screen)
            self.game.show_pieces(self.screen)
            self.game.show_possible_moves(self.screen)
            self.dragger.update_blit(self.screen)
        
        elif event.type == pygame.MOUSEBUTTONUP:
          self.dragger.undrag_piece()
          self.dragger.update_mouse(event.pos)
          clicked_row = self.dragger.mouse_y // SQUARE_SIZE
          clicked_col = self.dragger.mouse_x // SQUARE_SIZE
          self.game.move(clicked_row, clicked_col)
        
        elif event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
          
      pygame.display.update()
      
  def _get_square(self, row, col):
    return self.board.squares[row][col]

if __name__ == "__main__":
  Main().run()