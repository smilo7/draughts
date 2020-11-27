import pygame
from .constants import ALT_COLOUR, RED_CLICKED, SQUARE_SIZE, WIDTH

class Peice:
    def __init__(self, row, col, colour, window):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.window = window
        self.size = (WIDTH // 8) // 2.5
        self.direction = 0#forward 1 or backwards -1
        self.clicked = None

    def make_king(self):
        self.king = True

    def draw(self):
        back_size = self.size + 1
        pygame.draw.circle(self.window, ALT_COLOUR, (self.col * SQUARE_SIZE + back_size + back_size/4, self.row*SQUARE_SIZE + back_size + back_size/4), back_size)
        
        pygame.draw.circle(self.window, self.colour, (self.col * SQUARE_SIZE + self.size + self.size/4, self.row*SQUARE_SIZE + self.size + self.size/4), self.size)

    def draw_clicked(self):
        pygame.draw.circle(self.window, RED_CLICKED, (self.col * SQUARE_SIZE + self.size + self.size/4, self.row*SQUARE_SIZE + self.size + self.size/4), self.size)
