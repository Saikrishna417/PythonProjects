# Rules of the game
# Two players play the game against each other; let’s assume Player 1 and Player 2.

# Player 1 plays first by setting a multi-digit number.
# Player 2 now tries his first attempt at guessing the number.
# If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
# The game continues till Player 2 eventually is able to guess the number entirely.
# Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
# If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
# If not, then Player 2 wins the game.
# The real game, however, has proved aesthetics since the numbers are represented by color-coded buttons.

import random

def player_set_Num(Num):
    '''int --> int
     This function will seth number based on number of digits provided by user.
     >>> player_set_Num(4)
        1234
    '''
    return random.randint(10**(Num-1),10**(Num)-1)

def check_num(Num,guess_num):
    '''(int,int)-->bool
    This method will check if guess number is same original number or not.
    If not same then it will display how many correct letters
    '''
    if (guess_num == Num):
        print("Correctly guesses")
        return True
    else :
        empty = ''
        count = 0
        tmp1,tmp2 = str(Num),str(guess_num)
        for i in range(len(tmp1)):
            if tmp1[i] != tmp2[i]:
                empty = empty +'X'
            else:
                empty =empty + tmp1[i]
                count = count+1
        print(f'you have guessed {count} digits correctly, number with correct numbers {empty}')
        return False

def player_guess(Num):
    '''int --> int
    This function will check how many time player to gauss the number'''
    count = 0
    

    game_over = False

    while not(game_over):
        guess = int(input('Guess the number:\n'))
        game_over=check_num(Num,guess)
        count = count+1
    return count


def play():
    print('Player1  turn, Player1 is setting the number:\n')
    no_digits= int(input('How many digits number you want:\n'))
    Num = player_set_Num(no_digits)
    print('Player2  turn, player2 is gussing the  number:\n')
    score2=player_guess(Num)
    print('Player2  turn, Player2 is setting the number:\n')
    
    Num = player_set_Num(no_digits)
    print('Player1  turn, player1 is gussing the  number:\n')
    score1=player_guess(Num)
    if(score2 > score1):
        print(f"Player 1 is the winner.Player1 took {score1} chance to guess the number and Player2 took {score2} chance to guess the number")
    elif score2 < score1:
        print(f"Player 2 is the winner.Player1 took {score1} chance to guess the number and Player2 took {score2} chance to guess the number")
    else:
        print(f'Match is tie.Both Players took {score1} chance to guess the number ')

