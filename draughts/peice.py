import pygame
from .constants import OFF_WHITE, OFF_BLACK, SQUARE_SIZE

class Peice:
    def __init__(self, row, col, colour, window):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.window = window

    def make_king(self):
        self.king = True

    def draw(self):
        pygame.draw.circle(self.window, self.colour, (self.col * SQUARE_SIZE + 40 +10, self.row*SQUARE_SIZE +40 +10), 40)
