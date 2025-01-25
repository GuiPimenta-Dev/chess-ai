import pygame

from const import WIDTH, HEIGHT, SQUARE_SIZE

class Dragger:
  
  def __init__(self):
    self.piece = None
    self.dragging = False
    self.mouse_x = 0
    self.mouse_y = 0
    self.initial_row = 0
    self.initial_col = 0
  
  def update_blit(self, screen):
    pass
    
  
  def update_mouse(self, pos):
    self.mouse_x, self.mouse_y = pos
  
  def save_initial(self, pos):
    self.initial_row = pos[1] // SQUARE_SIZE
    self.initial_col = pos[0] // SQUARE_SIZE
  
  def drag_piece(self, piece):
    self.piece = piece
    self.dragging = True
  
  def undrag_piece(self):
    self.piece = None
    self.dragging = False