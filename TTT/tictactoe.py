"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0
    if board == initial_state():
        return X
    else:
        for x in range(3):
            for y in range(3):
                if board[x][y] == X:
                    count_X = count_X + 1
                elif board[x][y] == O:
                    count_O = count_O + 1

        if (count_X == count_O):
            return X
        else:
            return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    remaining = set()

    if board[0][0] == None:
        remaining.add((0, 0))

    for x in range(3):
        for y in range(3):
            if board[x][y] == None:
                remaining.add((x ,y))
    return remaining

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    for x in range(3):
        for y in range(3):
            if (x, y) == action:
                new_board[x][y] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x = 0
    
    if board[x][x] == board[x][x+1] == board[x][x+2] == X:
        return X   
    elif board[x][x] == board[x][x+1] == board[x][x+2] == O:
        return O  

    elif board[x+1][x] == board[x+1][x+1] == board[x+1][x+2] == X:
        return X 
    elif board[x+1][x] == board[x+1][x+1] == board[x+1][x+2] == O:
        return O  
    
    elif board[x+2][x] == board[x+2][x+1] == board[x+2][x+2] == X:
        return X 
    elif board[x+2][x] == board[x+2][x+1] == board[x+2][x+2] == O:
        return O

    elif board[x][x] == board[x+1][x] == board[x+2][x] == X:
        return X 
    elif board[x][x] == board[x+1][x] == board[x+2][x] == O:
        return O 
    
    elif board[x][x+1] == board[x+1][x+1] == board[x+2][x+1] == X:
        return X 
    elif board[x][x+1] == board[x+1][x+1] == board[x+2][x+1] == O:
        return O

    elif board[x][x+2] == board[x+1][x+2] == board[x+2][x+2] == X:
        return X
    elif board[x][x+2] == board[x+1][x+2] == board[x+2][x+2] == O:
        return O  

    elif board[x][x] == board[x+1][x+1] == board[x+2][x+2] == X:
        return X 
    elif board[x][x] == board[x+1][x+1] == board[x+2][x+2] == O:
        return O    
            
    elif board[x][x+2] == board[x+1][x+1] == board[x+2][x] == X:
        return X 
    elif board[x][x+2] == board[x+1][x+1] == board[x+2][x] == O:
        return O  

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    if winner(board) == None:
        for x in range(3):
            for y in range(3):
                if board[x][y] == EMPTY:
                    count += 1

        if count != 0:
            return False
        else:
            return True           

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def MIN_VALUE(b):
        if terminal(b) == True:
            return utility(b)
        else:
            v = math.inf
            for action in actions(b):
                x = result(b, action)
                n = MAX_VALUE(x)
                if v > n:
                    v = n
            return v

    def MAX_VALUE(b):
        if terminal(b) == True:
            return(utility(b))
        else:
            v = -math.inf
            for action in actions(b):
                y = result(b, action)
                m = MIN_VALUE(y)
                if v < m:
                    v = m
            return v

    optimal_action = (0, 0)
    a = 5
    
    for action in actions(board):
        if player(board) == X:
            if terminal(result(board, action)) == True:
                return action
            if a == 5:
                v = -math.inf
            a = MIN_VALUE(result(board, action))
            if  a > v:
                v = a
                optimal_action = action
            elif a == v:
                if terminal(result(board, action)) == True:
                    return action
        else:
            if terminal(result(board, action)) == True:
                print(action)
                return action
            if a == 5:
                v = math.inf
            a = MAX_VALUE(result(board, action))
            if a < v:
                v = a
                optimal_action = action
            elif a == v:
                if terminal(result(board, action)) == True:
                    return action
    return optimal_action






