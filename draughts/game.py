# Checkers game by cand no 184513
#knowledge and reasoning coursework november 2020
import pygame
from .board import Board
from .constants import BLACK, RED

class Game():
    def __init__(self, window, font):
        self.board = Board(8, 8, window)
        self.finished = False
        self.window = window #this is the pygame window
        self.turn = "R" # starting turn for red
        self.font = font


    def change_turn(self):
        if self.turn == "R":
            self.turn = "B"
        else:
            self.turn="R"

    def whos_turn_is_it(self):
        return self.turn

    def display_turns(self):
        if self.whos_turn_is_it() == "R":
            label = self.font.render("Red's Go", 1, RED)
            self.window.blit(label, (20, 850))
        elif self.whos_turn_is_it() == "B":
            label = self.font.render("Black's Go", 1, BLACK)
            self.window.blit(label, (20, 850))

    def display_taken_peices(self):
        reds_left = self.font.render("Reds left: " + str(self.board.red_peices), 1, RED)
        self.window.blit(reds_left, (20, 900))

        blacks_left = self.font.render("Blacks left: " + str(self.board.black_peices), 1, BLACK)
        self.window.blit(blacks_left, (150, 900))


    def display_controls(self):
        label = self.font.render("ESC to Quit, press R to restart", 1, BLACK)
        self.window.blit(label, (480, 960))

    def click(self, row, col):
        """
        When a mouse clicks this method is called
        which then calls the select_peice method in the board object
        """
        end_go = self.board.select_peice(row, col, self.turn)
        print(end_go)
        if end_go==True: #if endgo is true, a move has been made. change the turn. otherwise its just a click
            self.change_turn()
        else:
            pass


    #update loop
    def update(self):
        #draw board
        self.board.draw()
        self.display_turns()
        self.display_taken_peices()
        self.display_controls()
        #update display
        pygame.display.update()


#g = Game()
