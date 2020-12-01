# Checkers game by cand no 184513
#knowledge and reasoning coursework november 2020
import pygame
from .board import Board
from .constants import BLACK, RED, WIDTH, HEIGHT
from .minimax import draughts_AI

class Game():
    def __init__(self, window, font):
        self.board = Board(8, 8)
        self.finished = False
        self.window = window #this is the pygame window
        self.turn = "R" # starting turn for red
        self.font = font
        self.computer = draughts_AI()


    def change_turn(self):
        if self.turn == "R":
            self.turn = "B"
            #ai's turn
            #call minimax
            self.computer_move()
        else:
            self.turn="R"
            #players turn

    def computer_move(self):
        evaluation, new_board = self.computer.minimax(self.board, 5, True, alpha=float('-inf'), beta=float('inf'))
        #update board
        print("ai board", new_board)
        self.board = new_board
        print("ai move done")
        self.computer.states_searched = 0 #reset searched states
        self.change_turn()

    def whos_turn_is_it(self):
        return self.turn

    def display_turns(self):
        if self.whos_turn_is_it() == "R":
            label = self.font.render("Red's Go", 1, RED)
            self.window.blit(label, (WIDTH*0.01, HEIGHT*0.85))
        elif self.whos_turn_is_it() == "B":
            label = self.font.render("Black's Go", 1, BLACK)
            self.window.blit(label, (WIDTH*0.01, HEIGHT*0.85))

    def display_taken_peices(self):
        reds_left = self.font.render("Reds left: " + str(self.board.red_peices), 1, RED)
        self.window.blit(reds_left, (WIDTH*0.01, HEIGHT*0.9))

        blacks_left = self.font.render("Blacks left: " + str(self.board.black_peices), 1, BLACK)
        self.window.blit(blacks_left, (WIDTH*0.5, HEIGHT*0.9))


    def display_controls(self):
        label = self.font.render("ESC to Exit, R to Restart", 1, BLACK)
        self.window.blit(label, (WIDTH*0.3, HEIGHT*0.95))

    def display_winner():
        self.board

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
        self.board.draw(self.window)

        #menu stuff
        self.display_turns()
        self.display_taken_peices()
        self.display_controls()
        #update display
        pygame.display.update()


#g = Game()
