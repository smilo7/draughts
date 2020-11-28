import pygame
from .constants import ALT_COLOUR, RED_CLICKED, GREEN, SQUARE_SIZE, WIDTH

class Peice:
    def __init__(self, row, col, colour, direction, window):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.window = window
        self.size = (WIDTH // 8) // 2.5
        self.direction = direction #forward +1 or backwards -1
        self.clicked = None
        self.valid_moves = {"L": [], "R": []} #valid moves from peices current position, none by default (until clicked)

    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.row, self.col = row, col

    def has_valid_move(self):
        """
        Check if either left or right valid moves exist or there are none
        returns: True if there is any moves, returns False if there is no moves

        if self.valid_moves["L"] or self.valid_moves["R"]:
            return True
        return False
        """

        any_valid_moves = False
        for direction, moves in self.valid_moves.items():
            #print("HERE!", moves)
            if len(moves[0]) > 0:
                any_valid_moves = True
        return any_valid_moves

    def valid_move_for_direction(self, direction):
        if len(self.valid_moves[direction][0]) != 0:
            return True
        else:
            return False

    def is_valid_move(self, row, col):
        """
        if row and col is in the peices valid moves
        checks left then right valid moves
        """

        print(row, col)
        for move in self.valid_moves["L"]:
            if move[0][0] == row and move[0][1] == col:
                return True
            else:
                for move in self.valid_moves["R"]:
                    if move[0][0] == row and move[0][1] == col:
                        return True
        return False


    def draw(self):
        back_size = self.size + 1
        pygame.draw.circle(self.window, ALT_COLOUR, (self.col * SQUARE_SIZE + back_size + back_size/4, self.row*SQUARE_SIZE + back_size + back_size/4), back_size)

        pygame.draw.circle(self.window, self.colour, (self.col * SQUARE_SIZE + self.size + self.size/4, self.row*SQUARE_SIZE + self.size + self.size/4), self.size)

    def draw_clicked(self):
        pygame.draw.circle(self.window, RED_CLICKED, (self.col * SQUARE_SIZE + self.size + self.size/4, self.row*SQUARE_SIZE + self.size + self.size/4), self.size)

    def draw_valid_moves(self):
        """
        Draw valid moves by putting a nice circle there
        """

        for direction, moves in self.valid_moves.items():
            if (self.valid_move_for_direction(direction)):
                for move in moves:
                    move = move[0]
                    pygame.draw.circle(self.window, GREEN, (move[1]* SQUARE_SIZE + 20 + 20/4 , move[0]*SQUARE_SIZE + 20 + 20/4), 20)
