from pieces import Piece


class Rook(Piece):
    def __init__(self, id, direction, color, asset):
        super().__init__(
            id=id, name="Rook", direction=direction, color=color, asset=asset, value=5
        )

    def _get_possible_moves_in_each_direction(self, square, _):
        possible_moves = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for dr, dc in directions:
            directional_moves = []
            for i in range(1, 8):
                new_row = square.row + i * dr
                new_col = square.col + i * dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    directional_moves.append((new_row, new_col))
                else:
                    break

            if directional_moves:
                possible_moves.append(directional_moves)

        return possible_moves


class BlackRook(Rook):
    def __init__(self, id, direction):
        super().__init__(id, direction, "black", "black_rook.png")


class WhiteRook(Rook):
    def __init__(self, id, direction):
        super().__init__(id, direction, "white", "white_rook.png")
