import pygame
from .constants import BLACK, DARK_GREY, WHITE

class Button:
    """
    This makes button-like functionality for pygame.
    """
    def __init__(self, x, y, width, height, difficulty):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = BLACK
        self.clicked_colour = DARK_GREY
        self.pressed = False
        self.difficulty = difficulty


    def draw(self, window, font):
        pygame.draw.rect(window, self.colour, [self.x, self.y, self.width, self.height])
        label = font.render(self.difficulty, 1, WHITE)
        window.blit(label, (self.x+5, self.y+5))

    def clicked(self):
        #change colour
        self.colour = DARK_GREY
        print("CLICKED BUTTON")
        self.pressed = True

    def unclick(self):
        self.colour = BLACK

    def check_mouse(self, x, y):
        print("chcking mouse", x, y, self.x, self.y)

        if self.x < x < self.x+self.width and self.y < y < self.y+self.height:
            return True
        else:
            return False
