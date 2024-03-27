# User inputs the lower bound and upper bound of the range.
# The compiler generates a random integer between the range and store it in a variable for future references.
# For repetitive guessing, a while loop will be initialized.
# If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
# Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
# And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
# Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.

import random
import math

def get_range():
  low_range_val = int(input("Enter the lower limit bound for range:\t"))
  High_range_val = int(input("Enter the upper limit bound for range:\t"))
  return (low_range_val,High_range_val)


def randvalue_generator(low,up):
  return random.randint(low,up) 

low,up=get_range()
val=randvalue_generator (low,up)
min_guess = int(math.log2(up-low+1))

Game_over = False
count=0
while not(Game_over):
  print(f"You have {min_guess-count} chance too guess the number")
  guessed_num = int(input("Your choice gauess the number :\t"))
  count=count+1
  if (guessed_num>val):
    print("Your Guess is  high")
  elif(guessed_num < val):
    print("Your Guess is  Low")
  else:
    print(f"You Guessed correct. “Congratulations! ” You Have guessed in {count} chances")
    Game_over = True
  if count == min_guess and not(Game_over):
    Game_over = True
    print(f"Better Luck Next Time! ” You Have not guessed in {count} chances and Actual value is :{val}")
