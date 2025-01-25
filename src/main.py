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
  
  def run(self):
    while True:
      self.game.show_bg(self.screen)
      self.game.show_pieces(self.screen)
      
      for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          self.game.dragger.update_mouse(event.pos)
          clicked_row = self.game.dragger.mouse_y // SQUARE_SIZE
          clicked_col = self.game.dragger.mouse_x // SQUARE_SIZE
          
          if self.game.board.squares[clicked_row][clicked_col].has_piece():
            piece = self.game.board.squares[clicked_row][clicked_col].piece
            self.game.dragger.save_initial(event.pos)
            self.game.dragger.drag_piece(piece)
        
        elif event.type == pygame.MOUSEMOTION:
          if self.game.dragger.dragging:
            self.game.dragger.update_blit(self.screen)
        
        elif event.type == pygame.MOUSEBUTTONUP:
          pass
        
        elif event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
          
      pygame.display.update()

if __name__ == "__main__":
  Main().run()