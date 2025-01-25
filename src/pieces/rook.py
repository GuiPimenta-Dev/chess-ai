from pieces import Piece


class Rook(Piece):
    def __init__(self, id, color, asset):
        super().__init__(id, 'Rook', color, asset, 5)
        

class BlackRook(Rook):
    def __init__(self, id):
        super().__init__(id, 'black', 'black_rook.png')
        

class WhiteRook(Rook):
    def __init__(self, id):
        super().__init__(id, 'white', 'white_rook.png')