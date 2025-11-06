from typing import Any


import numpy as np
import random



board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])

players = ['X', 'O']
num_players = len(players)
Q = {} #states explored

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

# Function to choose an action based on the Q-table

#Random exploration condition in the choose_action function checks whether agent should perform a random exploration or not or if current state is not present in the Q-table
#if random exploration is choosen,
#a random action is chosen from the available empty cells on the board.
# This promotes exploration and allows the agent to try out different actions and gather more information about the environment.


#if exploitation is choosen,
#the function selects the action with the highest Q-value from the available empty cells.
#and do action - > update it with player symbol (X or O according to player(X or O according to current player)

def choose_action(board, exploration_rate):

    state = board_to_string(board)

    if random.uniform(0,1) < exploration_rate or state not in Q:

        #in this case we want to choose a random cell to play
        empty_cells = np.argwhere(board == '-')
        action = tuple(random.choice(empty_cells))
    else:
        #choose the action with highest Q value (argmaxQ(s,a) through all possible actions from state s)
        q_values = Q[state]
        empty_cells = np.argwhere(board == '-')
        empty_q_values = [q_values[cell[0],cell[1]] for cell in empty_cells]
        max_q_value = max(empty_q_values)
        







