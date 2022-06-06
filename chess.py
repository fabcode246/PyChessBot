import random
from valid_move import validate_move

class Chess:
    def __init__(self):
        self.cb = []
        for i in range(64):
            self.cb.append(0)

        self.killed = []

        self.black = 200
        self.white = 100

        self.pieces = {}

        self.piece_types = {
            10: 'pawn',
            20: 'bishop',
            30: 'knight',
            40: 'rook',
            50: 'queen',
            60: 'king'
        }
        self.make_pieces()

    def make_pieces(self):
        for clr in (100,200):
            for t in self.piece_types:
                row = 0 if clr == 200 else 8*7
                if t == 10:
                    for i in range(1, 9):
                        if clr == 100:
                            self.pieces[clr+t+i] = 8*6 + i
                            self.cb[(8*6+i)-1] = clr+t+i
                        if clr == 200:
                            self.pieces[clr+t+i] = i+8
                            self.cb[(8+i)-1] = clr+t+i
                
                if t == 20:
                    for i in (3,6):
                        self.pieces[clr+t+(i/3)] = row + i
                        self.cb[(row+i) -1] = clr+t+(i/3)
                        
                if t == 30:
                    for k, v in enumerate([2, 7]):
                        self.pieces[clr+t+(k+1)] = v + row
                        self.cb[(v+row) - 1] = clr+t+k+1

                if t == 40:
                    for k, v in enumerate([1, 8]):
                        self.pieces[clr+t+(k+1)] = v + row
                        self.cb[(v+row) - 1] = clr+t+k+1

                if t == 50:
                    self.pieces[clr+t+1] = row+4
                    self.cb[(4+row) - 1] = clr+t+1

                if t == 60:
                    self.pieces[clr+t+1] = row+5
                    self.cb[(row+5) - 1] = clr+t+1

    def make_move(self, tile, move):
        is_valid = validate_move(self.cb, tile, move)
        piece = self.cb[tile]
        if is_valid:
            if self.cb[move] != 0:
                killed = self.cb[move]
                self.pieces[killed] = 0
                self.killed.append(killed)
            self.cb[tile] = 0
            self.cb[move] = piece
            self.pieces[piece] = move
            return True
        else:
            return False
