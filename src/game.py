import pygame
from board import Board
from const import ROWS, COLS, SQUARE_SIZE
from dragger import Dragger

class Game:
    def __init__(self, play_as_white=True):
        self.play_as_white = play_as_white
        self.board = Board(play_as_white)
        self.dragger = Dragger()

    def show_bg(self, screen):
        
        for row in range(ROWS):
            for col in range(COLS):
                display_row = row if self.play_as_white else ROWS - 1 - row
                display_col = col if self.play_as_white else COLS - 1 - col
                
                if (display_row + display_col) % 2 == 0: 
                    color = (234, 235, 200)
                else:  
                    color = (119, 154, 88)

                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def show_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.squares[row][col]
                if square.has_piece():
                    img = pygame.image.load(square.piece.asset)
                    img_center = col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2
                    square.piece.texture_rect = img.get_rect(center=img_center)
                    screen.blit(img, square.piece.texture_rect)