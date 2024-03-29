import pygame
from .constants import WHITE, BLACK, RED, WIDTH, HEIGHT, LIGHT_GREY, DARK_GREY, GREEN
from .button import Button

class Menu:
    """
    This makes a menu for checkers game.
    """
    def __init__(self, x, y, width, height, font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = BLACK
        self.font = font
        self.buttons = self.make_buttons()
        self.instructions = Button(WIDTH*0.5, HEIGHT*0.95, 130, 80,"Controls/Rules")


    def draw(self, window, turn, num_peices):
        """
        Calls all related draw methods for the menu
        """
        #pygame.draw.rect(window, self.colour, [self.x, self.y, self.width, self.height])
        self.border(window)
        self.turns(window, turn)
        self.taken_peices(window, num_peices)
        #self.controls(window)
        self.draw_difficulty_buttons(window)
        self.difficulty_buttons_title(window)
        self.instructions.draw(window, self.font)
        if self.instructions.pop_up_win == True:
            self.instructions.draw_pop_up(window, self.font)


    def border(self, window):
        """
        Draws the menu border and background at the bottom of the screen
        """
        pygame.draw.rect(window, LIGHT_GREY, (0, self.width, self.width, self.height/4))
        pygame.draw.rect(window, DARK_GREY, (0, self.width, self.width, self.height/4), 4)

    def turns(self, window, turn):
        """
        Display a coloured circle depending on whos turn it is
        """
        title = self.font.render("Turn: ", 1, BLACK)
        window.blit(title, (WIDTH*0.01, HEIGHT*0.82))

        if turn == "R":
            pygame.draw.circle(window, RED, (WIDTH*0.15, HEIGHT*0.828), (WIDTH // 8) // 5)

        elif turn == "B":
            pygame.draw.circle(window, BLACK, (WIDTH*0.15, HEIGHT*0.828), (WIDTH // 8) // 5)

    def taken_peices(self, window, num_peices):
        """
        Display the number of peices left
        """
        reds_left = self.font.render("Red Pieces:    " + str(num_peices[0]), 1, RED)
        window.blit(reds_left, (WIDTH*0.01, HEIGHT*0.9))

        blacks_left = self.font.render("Black Pieces: " + str(num_peices[1]), 1, BLACK)
        window.blit(blacks_left, (WIDTH*0.01, HEIGHT*0.95))


    def controls(self, window):
        label = self.font.render("ESC to Exit, R to Restart", 1, BLACK)
        window.blit(label, (WIDTH*0.5, HEIGHT*0.95))

    def difficulty_buttons_title(self, window):
        """
        Display the title for the difficulty buttons
        """
        label = self.font.render("Difficulty:", 1, BLACK)
        window.blit(label, (WIDTH*0.5, HEIGHT*0.82))

    def make_buttons(self):
        """
        Create 3 button objects and append to list. These are the difficulty setting buttons
        returns list of buttons
        """
        buttons = []
        buttons.append(Button(WIDTH*0.5, HEIGHT*0.85, 50, 30,"Easy"))
        buttons.append(Button(WIDTH*0.65, HEIGHT*0.85, 50, 30,"Med"))
        buttons.append(Button(WIDTH*0.8, HEIGHT*0.85, 50, 30,"Hard"))
        return buttons

    def draw_difficulty_buttons(self, window):
        """
        Draws the difficulty setting buttons to screen using their draw method
        """
        for button in self.buttons:
            button.draw(window, self.font)

    def difficulty_buttons_click_handler(self, window, x, y):
        """
        Click handler for the difficulty buttons
        """
        for button in self.buttons:
            if button.check_mouse(x, y):
                button.clicked()
                return button.value
            else:
                button.unclick()

    def instructions_click_handler(self, window, x,y):
        """
        called to handle click events for the controls/Rules button
        has the special case of making the pop up display and dissapear
        """
        if self.instructions.check_mouse(x,y):
            self.instructions.clicked()
            self.instructions.pop_up_win = True
            return self.instructions.value
        else:
            self.instructions.pop_up_win = False
            self.instructions.unclick()
