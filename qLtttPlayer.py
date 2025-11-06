from typing import Any


import numpy as np
import random



board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])

players = ['X', 'O']
num_players = len(players)
Q = {}

learning_rate = 0.001
discount_factor = 0.9
exploration_rate = 0.5
num_episodes = 10000

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-------------')
    print_board(board)

#convert board state to a string so that it can be used as a key in the Q-table
def board_to_string(board):
    return ''.join(board.flatten())
board_to_string(board) #returns '---------'

#define action as a cell randomly selected from the empty cells
empty_cells = np.argwhere(board == '-') #returns an array of coordinates of empty cells
action = tuple(random.choice(empty_cells))
print(action)


# Function to check if the game is over by checking different winning condition

def is_game_over(board):

    # Check rows for winning condition
    for row in board:
        if len(set(row)) == 1 and row[0] != '-':        #len(set(row)) == 1 -> check if all elements in row are same and  none of the cell is empty
            return True, row[0]


    # Check columns
    for col in board.T:                                 #iterate over clms of transponse of board
        if len(set(col)) == 1 and col[0] != '-':
            return True, col[0]


    # Check diagonals
    if len(set(board.diagonal())) == 1 and board[0, 0] != '-':             #check all elements in main diagonal are same and non empty
        return True, board[0, 0]
    if len(set(np.fliplr(board).diagonal())) == 1 and board[0, 2] != '-':   #horizontal flip the board and check...
        return True, board[0, 2]


    # Check if the board is full
    if '-' not in board:
        return True, 'draw'

    return False, None







