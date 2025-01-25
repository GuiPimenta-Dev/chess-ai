from pieces import Piece


class Knight(Piece):
    def __init__(self, id, color, asset):
        super().__init__(id, 'Knight', color, asset, 3)
        

class BlackKnight(Knight):
    def __init__(self, id):
        super().__init__(id, 'black', 'black_knight.png')
        

class WhiteKnight(Knight):
    def __init__(self, id):
        super().__init__(id, 'white', 'white_knight.png')