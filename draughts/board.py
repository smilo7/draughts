import numpy as np
import pygame
from .constants import WHITE, BLACK, RED, ROWS, COLS, SQUARE_SIZE, DARK_BROWN, LIGHT_BROWN, BLACK_DIRECTION, RED_DIRECTION, RED_CLICKED, BLACK_CLICKED
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
        self.hopped_peices = {}
        self.red_peices = 0
        self.black_peices = 0
        self.force_hops = False


        self.make_board_pattern()
        self.display_text_board()
        self.put_in_peices()


    def evaluate(self):
        """
        calculates the score of the board
        """
        return self.red_peices - self.black_peices

    def return_board(self):
        return self.board


    def make_board_pattern(self):
        """
        makes the draughts board pattern in numerical form
        """
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

    def put_in_peices(self):
        """
        loops through the numerical representation and replaces neccassary
        spots with peices classes. 1 for BLACK and 2 for RED.
        """
        for row_i, row in enumerate(self.board):
            for col_i, col in enumerate(row):
                if (col == 1): #its a black peice!
                    self.board[row_i][col_i] = Peice(row_i, col_i, "B", BLACK, BLACK_CLICKED, BLACK_DIRECTION, self.window)
                    self.black_peices +=1
                elif (col == 2): #if its red
                    self.board[row_i][col_i] = Peice(row_i, col_i, "R", RED, RED_CLICKED, RED_DIRECTION, self.window)
                    self.red_peices += 1

    def display_text_board(self):
        """
        Display a text version of the board
        Returns a line by line printout
        """
        for line in self.board:
            print(line)

    def draw(self):
        """
        Draw function for the board. Deals with
        """
        self.draw_background()
        self.draw_peices()

        #draw clicked peice if there is one to draw
        if self.clicked_peice != None:
            self.clicked_peice.draw_clicked()
            self.clicked_peice.draw_valid_moves() #draw its valid moves if there is any




    def draw_background(self):
        """
        draws the backround of the draughts board
        """
        self.window.fill(LIGHT_BROWN)
        for row in range(0, ROWS):
            for col in range (row % 2, COLS, 2):
                pygame.draw.rect(self.window, DARK_BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_peices(self):
        """
        loop through board, if there is a peice draw it
        """
        for row in self.board:
            for peice in row:
                if peice != 0:
                    peice.draw()

    def select_peice(self, x, y, turn):
        """
        when a mouse selects a peice this function is called
        it then makes the selected peice the clicked_peice
        and checks for legal moves form this peice.
        """


        end_go = False

        #cast to int
        x = int(x)
        y = int(y)

        if (self.check_for_peice(x, y)):
            if (self.get_peice(x,y).type == turn): # check the peice that has been clicked is the current turn
                self.clicked_peice = self.get_peice(x, y)
                #check legal moves for this peice and store in its valid moves field
                self.clicked_peice.valid_moves = self.legal_moves(self.clicked_peice)

        #if a peice has not been clicked, check if there is any legal moves for that peice at the location clicked
        elif (self.clicked_peice != None): #make sure there is a currently selected peice
            if self.clicked_peice.valid_move_at_coords(x, y): #if peice contains x and y as a valid move
                self.move_peice(x, y)
                end_go = True
                #turn over a peice has been moved
        return end_go


    def move_peice(self, x, y):
        self.board[x][y] = self.clicked_peice #move peice on board
        self.board[self.clicked_peice.row][self.clicked_peice.col] = 0 #make old position empty
        #update peice coordinates
        self.clicked_peice.move(x, y)
        #take peices if there is any to take
        self.take_peices(self.clicked_peice)
        #make peice no longer "clicked" once moved
        self.clicked_peice = None
        #remove peices possible legal moves once it has moved
        #self.clicked_peice.clear_possible_moves()


    def take_peices(self, taker_peice):
        """
        takes peices based on start and end location of move
        peices inbetween will get removed.
        """
        if self.hopped_peices: #if its not empty
            for move, hopped in self.hopped_peices.items():
                if taker_peice.row == move[0] and taker_peice.col == move[1]:

                    #decrement the taken peices number
                    if (self.get_peice(hopped[0], hopped[1]).type == "R"):
                        self.red_peices -= 1
                    else:
                        self.black_peices -=1


                    self.delete_peice(hopped[0], hopped[1])
        else:
            pass

    def delete_peice(self, row, col):
        """
        removes a peice on the board if it exists at given row and col
        """
        if (self.check_for_peice(row,col)):
            self.board[row][col] = 0

    #check if peice is at coordinates
    def check_peice_colour(self, row, col):
        """
        return a peices colour if it exists at specific coordinates
        """
        if (self.board[row][col] != 0):
            peice = self.get_peice(row, col)
            return peice.colour
        else:
            return False

    def check_for_peice(self, row, col):
        """
        Check if peice exists at a given coordinate
        param: row, col
        returns: Bool
        """
        if (self.board[row][col] != 0):
            return True
        else:
            return False

    def get_peice(self, row, col):
        """
        Returns peice at given coordinate
        """
        if (self.board[row][col] != 0):
            return self.board[row][col]
        return None

    def check_in_board_size(self, row, col):
        """
        Check if coordinate is valid for the boards dimensions
        params: row, col
        returns: Bool
        """

        #row+1 due to index from 0..
        if ((row+1 > self.height or col+1 > self.width) or (row < 0 or col < 0)): #NEED TO CHECK IF ITS BIGGER OR SMALLER THAN
            return False
        return True


    def legal_moves(self, peice):
        moves = {"L": None, "R": None}
        moves["L"] = self.legal_moves_left(peice)
        moves["R"] = self.legal_moves_right(peice)

        #if forced jumping is on, then only return last move
        if self.force_hops:
            pass

        print(moves)
        return moves


    def legal_moves_left(self, peice):
    #def look_for_moves_left(self, peice):
        moves = []
        if peice.direction == +1 or peice.king: #forward (this is the player side)
            start_row, start_col = peice.row - 1, peice.col - 1
            moves.append(self.traverse_left(start_row, start_col, peice.colour, peice.direction, hop_count=0))

        elif(peice.direction == -1 or peice.king): #the AI aaaaaaa!
            start_row, start_col = peice.row + 1, peice.col + 1
            moves.append(self.traverse_left(start_row, start_col, peice.colour, peice.direction, hop_count=0))

        return moves

    def legal_moves_right(self, peice):
        moves = []
        if peice.direction == +1 or peice.king: #forward (this is the player side)
            start_row, start_col = peice.row - 1, peice.col + 1
            moves.append(self.traverse_right(start_row, start_col, peice.colour, peice.direction, hop_count=0))

        elif(peice.direction == -1 or peice.king): #the AI aaaaaaa!
            start_row, start_col = peice.row + 1, peice.col - 1
            moves.append(self.traverse_right(start_row, start_col, peice.colour, peice.direction, hop_count=0))

        return moves

    def traverse_left(self, start_row, start_col, peice_colour, direction, hop_count):
        moves = []

        #if its not in the board dont bother adding any possible moves
        if (self.check_in_board_size(start_row, start_col)):

            #if there is nothing there simply return the standard legt choice from that position (if a hop hasnt already been done)
            print("hop_count", hop_count)
            if (self.check_for_peice(start_row, start_col) != True):
                if (hop_count == 0):
                    moves.append( (start_row, start_col) )
            else:
                #there is a peice, then check what colour
                if (self.check_peice_colour(start_row, start_col) == peice_colour): #if its the same as peice colour, for the peice we are checking
                    #no possible move return nothing
                    pass
                else:

                    #calculate the possible hop location based on direction of peice
                    if direction == +1:
                        start_row-=1
                        start_col-=1
                    else:
                        start_row+=1
                        start_col+=1

                    #check that the possible hop location is within the board dimensions

                    #check there isnt a peice at the hop location and check that the possible hop is in range
                    if (self.check_in_board_size(start_row, start_col)):
                        #check if there is a peice there
                        if (not self.check_for_peice(start_row, start_col)):
                            moves.append( (start_row, start_col) )

                            #peice should be taken now at the location behind the hop
                            if direction == +1:
                                #add the possible move, and the hopped peice
                                self.hopped_peices[(start_row,start_col)] = (start_row+1, start_col+1)
                            else:
                                self.hopped_peices[(start_row,start_col)] = (start_row-1, start_col-1)

                            #call traverse function again from the sqaure beyond it to see if there is another hop possible

                            if direction == +1:
                                start_row-=1
                                start_col-=1
                            else:
                                start_row+=1
                                start_col+=1

                            #increase hop count
                            hop_count += 1
                            moves += ( (self.traverse_left(start_row, start_col, peice_colour, direction, hop_count)) )
                            #moves.append(self.traverse_left(start_row, start_col, peice_colour, direction)[0])
                            #moves.append(self.traverse_left(start_row, start_col, peice_colour, direction)[1])
                        else:
                            pass

        return moves

    def traverse_right(self, start_row, start_col, peice_colour, direction, hop_count):
        moves = []

        #if its not in the board dont bother adding any possible moves
        if (self.check_in_board_size(start_row, start_col)):

            #if there is nothing there simply return the standard legt choice from that position (if a hop hasnt already been done)
            print("hop_count", hop_count)
            if (self.check_for_peice(start_row, start_col) != True):
                if (hop_count == 0):
                    moves.append( (start_row, start_col) )
            else:
                #there is a peice, then check what colour
                if (self.check_peice_colour(start_row, start_col) == peice_colour): #if its the same as peice colour, for the peice we are checking
                    #no possible move return nothing
                    pass
                else:

                    #calculate the possible hop location based on direction of peice
                    if direction == +1:
                        start_row-=1
                        start_col+=1
                    else:
                        start_row+=1
                        start_col-=1

                    #check that the possible hop location is within the board dimensions

                    #check there isnt a peice at the hop location and check that the possible hop is in range
                    if (self.check_in_board_size(start_row, start_col)):
                        #check if there is a peice there
                        if (not self.check_for_peice(start_row, start_col)):
                            moves.append( (start_row, start_col) )

                            #peice should be taken now at the location behind the hop
                            if direction == +1:
                                self.hopped_peices[(start_row,start_col)] = (start_row+1, start_col-1)
                            else:
                                self.hopped_peices[(start_row,start_col)] = (start_row-1, start_col+1)

                            #call traverse function again from the sqaure beyond it to see if there is another hop possible

                            if direction == +1:
                                start_row-=1
                                start_col+=1
                            else:
                                start_row+=1
                                start_col-=1

                            #increase hop count
                            hop_count += 1
                            moves += ( (self.traverse_right(start_row, start_col, peice_colour, direction, hop_count)) )
                            #moves.append(self.traverse_left(start_row, start_col, peice_colour, direction)[0])
                            #moves.append(self.traverse_left(start_row, start_col, peice_colour, direction)[1])
                        else:
                            pass

        return moves
