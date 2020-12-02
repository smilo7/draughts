import pygame
from .constants import ALT_COLOUR, RED_CLICKED, GREEN, SQUARE_SIZE, WIDTH, ROWS, COLS

class Peice:
    def __init__(self, row, col, type, colour, clicked_colour, direction):
        self.row = row
        self.col = col
        self.type = type #"R" or "B" for red or black
        self.colour = colour
        self.clicked_colour = clicked_colour
        self.king = False
        #self.window = window
        self.size = (WIDTH // 8) // 2.5
        self.direction = direction #forward +1 or backwards -1
        self.clicked = None
        self.valid_moves = {"L": [], "R": []} #valid moves from peices current position, none by default (until clicked)
        self.hops = {"L": [], "R": []}

    def check_make_king(self):
        if (self.direction == -1):
            if (self.row == ROWS-1):
                self.king = True
        elif (self.direction == +1):
            if (self.row == 0):
                self.king = True

    def move(self, row, col):
        self.row, self.col = row, col
        #check if its at the kingrow to make king (depending on direction)
        self.check_make_king()
        #print("King!", self.king)

    def clear_possible_moves(self):
        self.valid_moves = {"L": [], "R": []}

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
            for move in moves:
                if len(move[0]) > 0:
                    any_valid_moves = True
        return any_valid_moves

    def valid_move_for_direction(self, direction):
        """
        if there is one or more valid moves for a given direction (left or right)
        return true, otherwise false
        """
        for move in self.valid_moves[direction]:
            if len(move) !=0:
                return True
            else:
                return False
            """
            if len(self.valid_moves[direction][0]) != 0:
                return True
            else:
                return False
            """



    def valid_move_at_coords(self, row, col):
        """
        are the given coordinates (row, col) a valid move for this peice?
        return true or false

        valid = False
        for direction, moves in self.valid_moves.items():
            if (self.valid_move_for_direction(direction)):
                for move in moves:
                    if len(move) !=0:

                        if move[0][0] == row and move[0][1] == col:
                            valid = True
                            print("VALID", valid)
        """

        valid = False
        for direction, moves in self.valid_moves.items():
            for move in moves:
                if move:
                    if move[0][0] == row and move[0][1] == col:
                        valid = True
        return valid


    def draw(self, window):

        back_size = self.size + 1
        pygame.draw.circle(window, ALT_COLOUR, (self.col * SQUARE_SIZE + back_size + back_size/4, self.row*SQUARE_SIZE + back_size + back_size/4), back_size)

        pygame.draw.circle(window, self.colour, (self.col * SQUARE_SIZE + self.size + self.size/4, self.row*SQUARE_SIZE + self.size + self.size/4), self.size)
        if self.king:
            crown = pygame.image.load('crown.png')
            window.blit(crown, (self.col * SQUARE_SIZE + self.size-7,self.row * SQUARE_SIZE + self.size-7))


    def draw_clicked(self, window):
        pygame.draw.circle(window, self.clicked_colour, (self.col * SQUARE_SIZE + self.size + self.size/4, self.row*SQUARE_SIZE + self.size + self.size/4), self.size)

    def draw_valid_moves(self, window):
        """
        Draw valid moves by putting a nice circle there
        """

        #for direction, moves in self.valid_moves.items():
    #        if

        for direction, moves in self.valid_moves.items():
            if (self.valid_move_for_direction(direction) or self.king):
                #only draw the last move
                #print(moves[0][-1])
                for move in moves:

                    #print(move[0])
                    if (len(move)!=0):
                        #print("drawing", move)
                        move = move[0]
                        pygame.draw.circle(window, GREEN, (move[1]* SQUARE_SIZE + self.size + self.size/4, move[0]* SQUARE_SIZE + self.size + self.size/4), self.size)
                        #pygame.draw.circle(window, GREEN, (move[1]* SQUARE_SIZE + 20 + 20/4 , move[0]*SQUARE_SIZE + 20 + 20/4), 20)
