from pieces import Piece


class Bishop(Piece):
    def __init__(self, id, color, asset):
        super().__init__(id, 'Bishop', color, asset, 3)
        

class BlackBishop(Bishop):
    def __init__(self, id):
        super().__init__(id, 'black', 'black_bishop.png')
        

class WhiteBishop(Bishop):
    def __init__(self, id):
        super().__init__(id, 'white', 'white_bishop.png')