# Checkers game by cand no 184513
#knowledge and reasoning coursework november 2020
import pygame
from .board import Board


class Game():
    def __init__(self, window):
        self.board = Board(8, 8, window)
        self.finished = False
        self.window = window #this is the pygame window

    def begin_game(self):
        board.display_text_board()
        #while(!self.finished): #while the game isnt finished
    #        self.ask_player_for_move()

    def ask_player_for_move(self):
        move = input("choose a coordinate to move to:")
        #check if player wants to quit first
        if (move == "exit"):
            self.finished = True
        if (self.validate_move(move)):
            board.update_board()

        #move (x, y)

    def validate_move(self, move):
        #check format
        for char in move:
            print(char)
        return Move(row,col)
        #check its within Board

    def click(self, row, col):
        """
        When a mouse clicks this method is called
        which then calls the select_peice method in the board object
        """
        self.board.select_peice(row, col)

    #update loop
    def update(self):
        #draw board
        self.board.draw()
        #update display
        pygame.display.update()


#g = Game()
