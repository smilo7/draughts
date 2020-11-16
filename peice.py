class Peice:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False


    def make_king(self):
        self.king = True
