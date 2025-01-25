from pieces import Piece


class King(Piece):
    def __init__(self, id, color, asset):
        super().__init__(id, 'Queen', color, asset)
        

class BlackKing(King):
    def __init__(self, id):
        super().__init__(id, 'black', 'black_king.png')
        

class WhiteKing(King):
    def __init__(self, id):
        super().__init__(id, 'white', 'white_king.png')