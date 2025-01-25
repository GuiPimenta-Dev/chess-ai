from pieces import Piece


class Queen(Piece):
    def __init__(self, id, color, asset):
        super().__init__(id, 'Queen', color, asset, 9)
        

class BlackQueen(Queen):
    def __init__(self, id):
        super().__init__(id, 'black', 'black_queen.png')
        

class WhiteQueen(Queen):
    def __init__(self, id):
        super().__init__(id, 'white', 'white_queen.png')