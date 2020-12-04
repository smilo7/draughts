import pygame
from .constants import BLACK, DARK_GREY, WHITE

class Button:
    """
    This makes button-like functionality for pygame.
    """
    def __init__(self, x, y, width, height, value="Hard"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = BLACK
        self.clicked_colour = DARK_GREY
        self.pressed = False
        self.value = value
        self.pop_up_win = False


    def draw(self, window, font):
        pygame.draw.rect(window, self.colour, [self.x, self.y, self.width, self.height])
        pygame.draw.rect(window, DARK_GREY, [self.x, self.y, self.width, self.height], 2)
        label = font.render(self.value, 1, WHITE)
        window.blit(label, (self.x+5, self.y+5))

    def clicked(self):
        #change colour
        self.colour = DARK_GREY
        print("CLICKED BUTTON")
        self.pressed = True

    def unclick(self):
        self.colour = BLACK

    def check_mouse(self, x, y):
        #print("chcking mouse", x, y, self.x, self.y)

        if self.x < x < self.x+self.width and self.y < y < self.y+self.height:
            return True
        else:
            return False

    def draw_pop_up(self, window, font):
        pygame.draw.rect(window, WHITE, (0, 0, 400, 400))

        text = font.render("Press ESC to quit, R to restart", 1, BLACK)
        text2 = font.render("Rules:", 1, BLACK)
        text_width, text_height = text.get_size()
        text_rect = text.get_rect(center=(400/2,10))
        window.blit(text, text_rect)
