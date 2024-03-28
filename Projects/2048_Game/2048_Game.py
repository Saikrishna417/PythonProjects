import random

def board_display(board):
    '''This method will display a 4x4 board in matrix form, with empty spaces represented by 0'''
   
    print("-------"*4)
    for i in range(4):
        for j in range(4):
            print('|_ ', end='')
            if board[i][j] == 0:
                print(' ', end='')
            else:
                print(board[i][j], end='')
            print(' _|', end='')
        print('\n' + "-------"*4)
    return 0
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#board_display(board)

def check_winner(board):
    '''If any of the value contains 2048 then player is winner'''
    Winner = False
    for i in range(0,4,1):
        Winner = 2048 in board[i]
        if Winner == True:
            break
    return Winner


def player_input():
    '''This function will return the user entered values
    w or W for up
    s or S for down
    a or A for left
    d or D for right 
    any other inputs given then user has to select again
    '''
    valid_inputs = ['w','W','s','S','a','A','d','D']
    valid = False
    while not(valid):
        ch=input('Enter the valid inputs only :\n')[0]
        valid = ch in valid_inputs
    return ch

def new_value_insert(board):
    '''This function will insert the new value in the empty cell'''
    Value=2**random.randint(1,4)
    value_insert = False
    board_display(board)
    while not(value_insert):
        i = random.randint(0,3)
        j= random.randint(0,3)
        print(i,j)
        print(board[i][j])
        if board[i][j] == 0:
            board[i][j] = Value
            value_insert = True
    return board

