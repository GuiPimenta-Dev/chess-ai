from pieces import Piece


class Pawn(Piece):
    def __init__(self, id, color, asset):
        super().__init__(id, 'Pawn', color, asset, 1)
        

class BlackPawn(Pawn):
    def __init__(self, id):
        super().__init__(id, 'black', 'black_pawn.png')
        

class WhitePawn(Pawn):
    def __init__(self, id):
        super().__init__(id, 'white', 'white_pawn.png')