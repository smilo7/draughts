import numpy as np
import pygame
from .constants import WHITE, BLACK, RED, ROWS, COLS, SQUARE_SIZE, DARK_BROWN, LIGHT_BROWN
from .peice import Peice



class Board():

    def __init__(self, width, height, window):
        self.board = np.zeros(shape=(width, height)).astype(int).tolist()
        #board background
        self.backboard = np.zeros(shape=(width, height)).astype(int).tolist()
        self.width = width
        self.height = height
        self.square_size = 800 / width
        self.window = window
        self.clicked_peice = None

        self.make_board_pattern()
        self.display_text_board()

        self.put_in_peices()


    def make_board_pattern(self):
        #makes board representations
        for i in range(0, self.width):
            player = 1
            if (i > 2 and i <= 4):
                player = 0
            elif (i > 4):
                player = 2

            if ((i % 2) == 0): #even
                for j in range(0, self.width):
                    if ((j % 2) != 0):
                        self.board[i][j] = player
                        self.backboard[i][j] = -1
            if ((i % 2) != 0): #odd
                for j in range(0, self.width):
                    if ((j%2)==0):
                        self.board[i][j] = player
                        self.backboard[i][j] = -1

    #replace the numbers on the board with peice objects
    def put_in_peices(self):
        for row_i, row in enumerate(self.board):
            for col_i, col in enumerate(row):
                if (col == 1): #its a black peice!
                    self.board[row_i][col_i] = Peice(row_i, col_i, BLACK, self.window)
                elif (col == 2): #if its white
                    self.board[row_i][col_i] = Peice(row_i, col_i, RED, self.window)

    def display_text_board(self):
        for line in self.board:
            print(line)

    def draw(self):
        self.draw_background()
        self.draw_peices()
        if self.clicked_peice != None:
            self.clicked_peice.draw_clicked()


    def draw_background(self):
        self.window.fill(LIGHT_BROWN)
        #pygame.draw.rect(self.window, WHITE, (0,0, 200,200))
        for row in range(0, ROWS):
            for col in range (row % 2, COLS, 2):
                pygame.draw.rect(self.window, DARK_BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_peices(self):
        #loop through board, if there is a peice draw it
        for row in self.board:
            for peice in row:
                if peice != 0:
                    peice.draw()
        """
        #loop through board and depending on the number draw white or black peices
        for row_i, row in enumerate(self.board):
            for col_i, col in enumerate(row):
                if (col == 1): #its a black peice!
                    self.peices.append(Peice(row_i, col_i, BLACK, self.window))
                    self.peices[-1].draw()
                elif(col == 2):
                    self.peices.append(Peice(row_i, col_i, RED, self.window))
                    self.peices[-1].draw()
        """

    def select_peice(self, x, y):

        for row in self.board:
            for peice in row:
                if peice != 0: # if there is a peice there
                    if peice.row == x and peice.col == y:
                        print(peice, x, y)
                        self.clicked_peice = peice

        """
        for peice in self.peices:
            if (peice.row == row and peice.col == col):
                print(peice, row, col)
                self.clicked_peice = peice
                peice.draw_clicked()
        """

    def legal_moves(self, peice):
        #check if hop is available
        return 0

    def update_board(self, player, move):
        #update internal
        return 0
        #update display
