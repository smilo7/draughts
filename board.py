import numpy as np
import pygame

class Board():

    def __init__(self, width, height):
        self.board = np.zeros(shape=(width, height)).astype(int).tolist()
        self.width = width
        self.height = height

        #makes board representation
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
            if ((i % 2) != 0): #odd
                for j in range(0, width):
                    if ((j%2)==0):
                        self.board[i][j] = player

    def display_text_board(self):
        for line in self.board:
            print(line)
    def draw_background(self, window):
        window.fill()


    def update_board(self, player, move):
        #update internal
        return 0
        #update display
