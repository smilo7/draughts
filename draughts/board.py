import numpy as np
import pygame
from .constants import WHITE, BLACK, OFF_BLACK, OFF_WHITE, ROWS, COLS, SQUARE_SIZE
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
        self.peices = []

        #makes board representations
        for i in range(0, width):
            player = 1

            if (i > 2 and i <= 4):
                player = 0
            elif (i > 4):
                player = 2

            if ((i % 2) == 0): #even
                for j in range(0, width):
                    if ((j % 2) != 0):
                        self.board[i][j] = player
                        self.backboard[i][j] = -1
            if ((i % 2) != 0): #odd
                for j in range(0, width):
                    if ((j%2)==0):
                        self.board[i][j] = player
                        self.backboard[i][j] = -1

        self.display_text_board()


    def display_text_board(self):
        for line in self.board:
            print(line)

    def draw(self):
        self.draw_background()
        self.draw_peices()

    def draw_background(self):
        self.window.fill(WHITE)
        #pygame.draw.rect(self.window, WHITE, (0,0, 200,200))
        for row in range(0, ROWS):
            for col in range (row % 2, COLS, 2):
                pygame.draw.rect(self.window, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_peices(self):
        #loop through board and depending on the number draw white or black peices
        for row_i, row in enumerate(self.board):
            for col_i, col in enumerate(row):
                if (col == 1): #its a black peice!
                    self.peices.append(Peice(row_i, col_i, OFF_BLACK, self.window))
                    self.peices[-1].draw()
                elif(col == 2):
                    self.peices.append(Peice(row_i, col_i, OFF_WHITE, self.window))
                    self.peices[-1].draw()



    def update_board(self, player, move):
        #update internal
        return 0
        #update display
