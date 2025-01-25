import pygame
from board import Board
from const import ROWS, COLS, SQUARE_SIZE
from dragger import Dragger
from move import Move
from pieces import Piece
from pieces.pawn import Pawn
from square import Square


class Game:
    def __init__(self, play_as_white=True):
        self.play_as_white = play_as_white
        self.hovered_square = None
        self.board = Board(play_as_white)
        self.dragger = Dragger()
        self.turn = "white"
        self.last_move = None
        self.possible_moves = []

    def show_bg(self, screen):

        for row in range(ROWS):
            for col in range(COLS):
                display_row = row if self.play_as_white else ROWS - 1 - row
                display_col = col if self.play_as_white else COLS - 1 - col

                if (display_row + display_col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                pygame.draw.rect(
                    screen,
                    color,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def show_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.squares[row][col]
                if square.has_piece() and square.piece != self.dragger.piece:
                    img = pygame.image.load(square.piece.asset)
                    img_center = (
                        col * SQUARE_SIZE + SQUARE_SIZE // 2,
                        row * SQUARE_SIZE + SQUARE_SIZE // 2,
                    )
                    square.piece.texture_rect = img.get_rect(center=img_center)
                    screen.blit(img, square.piece.texture_rect)

    def show_last_move(self, screen):
        if self.last_move:
            initial_row = self.last_move.initial_row
            initial_col = self.last_move.initial_col
            target_row = self.last_move.target_row
            target_col = self.last_move.target_col

            initial_rect = (initial_col * SQUARE_SIZE, initial_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            target_rect = (target_col * SQUARE_SIZE, target_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            
            color = (172, 195, 51)
            pygame.draw.rect(screen, color, initial_rect)
            pygame.draw.rect(screen, color, target_rect)

    def set_possible_moves(self, row, col):
        piece = self.board.squares[row][col].piece
        initial_square = Square(row, col, piece)
    

        if not isinstance(initial_square.piece, Pawn):

            possible_moves = initial_square.piece.possible_moves(
                initial_square.row, initial_square.col
            )

            for possible_direction in possible_moves:
                for possible_square in possible_direction:
                    target_square = self.board.squares[possible_square[0]][
                        possible_square[1]
                    ]

                    if not target_square.has_piece():
                        self.possible_moves.append(
                            Move(
                                initial_row=initial_square.row,
                                initial_col=initial_square.col,
                                target_row=possible_square[0],
                                target_col=possible_square[1],
                                piece=initial_square.piece,
                            )
                        )
                    elif target_square.has_enemy(initial_square.piece):
                        self.possible_moves.append(
                            Move(
                                initial_row=initial_square.row,
                                initial_col=initial_square.col,
                                target_row=possible_square[0],
                                target_col=possible_square[1],
                                piece=initial_square.piece,
                                captured_piece=target_square.piece,
                            )
                        )
                        break
                    else:
                        break

        else:
            possible_moves = initial_square.piece.possible_moves(
                initial_square.row, initial_square.col
            )
            for possible_direction in possible_moves:
                for possible_square in possible_direction:
                    target_square = self.board.squares[possible_square[0]][
                        possible_square[1]
                    ]

                    if not target_square.has_piece():
                        self.possible_moves.append(
                            Move(
                                initial_row=initial_square.row,
                                initial_col=initial_square.col,
                                target_row=possible_square[0],
                                target_col=possible_square[1],
                                piece=initial_square.piece,
                            )
                        )
                    else:
                        break

            possible_attacks = initial_square.piece.possible_attacks(
                initial_square.row, initial_square.col
            )
            for possible_direction in possible_attacks:
                for possible_square in possible_direction:
                    target_square = self.board.squares[possible_square[0]][
                        possible_square[1]
                    ]
                    if target_square.has_enemy(initial_square.piece):
                        self.possible_moves.append(
                            Move(
                                initial_row=initial_square.row,
                                initial_col=initial_square.col,
                                target_row=possible_square[0],
                                target_col=possible_square[1],
                                piece=initial_square.piece,
                                captured_piece=target_square.piece,
                            )
                        )

    def move(self, row, col):
        square = self.board.squares[row][col]
        move = self._find_move(square.row, square.col)
        if not move:
            self._reset_possible_moves()
            return

        self.board.move(self.possible_moves, move)
        self.last_move = move
        self.dragger.undrag_piece()
        self._switch_turn()
        self._reset_possible_moves()

    def show_hover(self, surface):
        if self.hovered_square:
            color = (180, 180, 180)
            rect = (self.hovered_square.col * SQUARE_SIZE, self.hovered_square.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(surface, color, rect, width=3)

    def set_hover(self, row, col):
        self.hovered_square = self.board.squares[row][col]
    
    def _switch_turn(self):
        self.turn = "white" if self.turn == "black" else "black"

    def _find_move(self, row, col):
        for move in self.possible_moves:
            if move.target_row == row and move.target_col == col:
                return move
        return None

    def _reset_possible_moves(self):
        self.possible_moves = []

    def show_possible_moves(self, screen):
        for move in self.possible_moves:
            center_x = move.target_col * SQUARE_SIZE + SQUARE_SIZE // 2
            center_y = move.target_row * SQUARE_SIZE + SQUARE_SIZE // 2
            radius = SQUARE_SIZE // 4
            color = (100, 100, 100, 60) if not move.captured_piece else (200, 100, 100)
            pygame.draw.circle(screen, color, (center_x, center_y), radius)
