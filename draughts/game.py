# Checkers game by cand no 184513
#knowledge and reasoning coursework november 2020
import pygame
from .board import Board
from .constants import BLACK, RED, WIDTH, HEIGHT
from .minimax import draughts_AI
from .menu import Menu
import time

class Game():
    def __init__(self, window, font):
        self.board = Board(8, 8)
        self.finished = False
        self.window = window #this is the pygame window
        self.turn = "R" # starting turn for red
        self.font = font
        self.computer = draughts_AI()
        self.menu = Menu(WIDTH, HEIGHT-(HEIGHT-WIDTH), WIDTH, HEIGHT-(HEIGHT-WIDTH), self.font)
        self.search_depth = 5


    def change_turn(self):
        if self.turn == "R":
            self.turn = "B"
            #ai's turn
            #call minimax
            self.update() #call update here so that screen and menu updates before the major lag of the ai lol
            #self.menu.turns(self.window, self.whos_turn_is_it())
            #pygame.display.update() #call display update otherwise move isnt refreshed intime to duisplay on menu
            self.computer_move()


        else:
            self.turn="R"
            #players turn


    def computer_move(self):
        print("SEARCHING WITH DIFFICULTY", self.search_depth)
        evaluation, new_board = self.computer.minimax(self.board, self.search_depth, True, alpha=float('-inf'), beta=float('inf'))
        #update board
        print("minimax eval", evaluation)
        if new_board != None:
            """
            sometimes the ai will return None if it doesnthave any possible moves left. This is a possible win state
            """
            print("ai board", new_board)
            self.board = new_board
            print("ai move done")
            self.computer.states_searched = 0 #reset searched states
        else:
            #get the winner no possible states left
            print("the winner is:", self.board.get_winner())
        #time.sleep(1000)
        self.change_turn()

    def whos_turn_is_it(self):
        return self.turn

    def set_difficulty(self, difficulty):
        """
        Changes the search depth given a difficulty rating
        """
        if difficulty == "Easy":
            self.search_depth = 1
            self.computer.update_difficulty(self.search_depth, difficulty)
        elif difficulty == "Med":
            self.search_depth = 3
            self.computer.update_difficulty(self.search_depth, difficulty)
        elif difficulty == "Hard":
            self.search_depth = 5
            self.computer.update_difficulty(self.search_depth, difficulty)

    def click(self, row, col):
        """
        When a mouse clicks this method is called
        which then calls the select_peice method in the board object
        """
        end_go = self.board.select_peice(row, col, self.turn)

        if end_go==True: #if endgo is true, a move has been made. change the turn. otherwise its just a click
            self.change_turn()
        else:
            pass


    #update loop
    def update(self):
        #draw board
        self.board.draw(self.window)
        #menu stuff
        self.menu.draw(self.window, self.whos_turn_is_it(), (self.board.red_peices, self.board.black_peices))
        #update display
        pygame.display.update()


#g = Game()
