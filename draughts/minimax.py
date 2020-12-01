from copy import deepcopy

MAX_DEPTH = 3

states_searched = 0
class draughts_AI:
    def __init__(self):
        self.states_searched = 0
        self.depth = MAX_DEPTH


    def minimax(self, current_board, current_depth, is_max, alpha, beta):

        """
        params: board - current board
        assumes max player is red and min player is black
        """

        #print("evaluating", current_depth)
        self.states_searched+=1
        #base case, once this is hit the recursion unravels.
        if current_depth == 0 or current_board.get_winner() != None:
            #print("SEARCHED,", self.states_searched)
            return current_board.evaluate(), current_board#return the score

        #black is the maximiser as this is the colour our ai plays
        if is_max:
            max_evaluation = float('-inf') #anything better than negative infinity will replace this :)
            best_state = None #stores the current bestboard
            for possible_state in self.moves_for_a_board(current_board, "B"): #get all possible board states
                evaluation = self.minimax(possible_state, current_depth-1, False, alpha, beta)[0]
                max_evaluation = max(max_evaluation, evaluation) #see if evaluation made above is better than the current max_evaluation. if so update max_evaluation
                alpha = max(max_evaluation, alpha)
                if beta <= alpha:
                    break
                if max_evaluation == evaluation: #if the max_evaluation is the same as the current one, then update the running best possible state/move
                    best_state = possible_state
            return max_evaluation, best_state
            #print(max_evaluation, best_state)
        #mimiser (red)
        else:
            min_evaluation = float('inf') #anything better than negative infinity will replace this :)
            best_state = None
            for possible_state in self.moves_for_a_board(current_board, "R"): #get all possible board states
                evaluation = self.minimax(possible_state, current_depth-1, True, alpha, beta)[0]
                min_evaluation = min(min_evaluation, evaluation) #see if evaluation made above is better than the current max_evaluation. if so update max_evaluation
                beta = min(beta, min_evaluation)
                if beta <= alpha:
                    break
                if min_evaluation == evaluation: #if the max_evaluation is the same as the current one, then update the running best possible state/move
                    best_state = possible_state
            #print(min_evaluation, best_state)
            return min_evaluation, best_state


    def moves_for_a_board(self, board, peice_type):
        """
        gets all possible board states by looking at every possible move from the given board.
        then returns a list of these boards
        """

        possible_board_states = []
        #for each peice on the given board get all possible legal moves for that peice
        for peice in board.return_all_peices_type(peice_type):
            legal_moves = board.legal_moves(peice)
            #loop through all the legal moves, left and right directions :)
            for direction, moves in legal_moves.items():
                #for each move in each direction
                #check if there are actually any moves
                #print("MOVES",moves)
                if len(moves[0]) != 0:

                #if (peice.valid_move_for_direction(direction) or peice.king):
                    for move in moves:
                        if len(move) !=0:
                            #print("MOVE", move)
                            move = move[0] #access the tuple in the list
                            copied_board = deepcopy(board) #copy the board
                            copied_peice = copied_board.get_peice(peice.row, peice.col) #make a copy of the peice so we don't mess with the original boards peice
                            new_board = self.mock_move(copied_board, copied_peice, move) #make a mock_move on the copied board and store it in new_board
                            possible_board_states.append(new_board)
        #print(possible_board_states)
        return possible_board_states


    def mock_move(self, board, peice, move):
        """
        For making mock/simulated moves on a board for a given peice and move
        makes sure to take any peices if there is any to take
        returns the updated board
        """
        row = move[0]
        col = move[1]
        #print(row, col)

        board.board[row][col] = peice #move peice on board
        board.board[peice.row][peice.col] = 0 #make old position empty

        #take peices if there are any
        board.take_peices_diagonal(peice, (row, col))

        #update peice coordinates for the peice
        peice.move(row, col)
        return board
