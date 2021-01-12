from random import *
from functions import *

turns = 10
correct = False
number = randint(1, 1000)


pw()


print("""
Welcome to Higher or Lower!
The goal of this game is to
guess a number between 1 and 1000
before you run out of turns

After each guess, you are given
either \"Higher\" or \"Lower\" 
to guide you in the right direction
""")


print(f"""
Lets see your skill {username}!
You have {turns} guesses available
Guess the number correctly within those guesses and you win!
""")


while correct is False and turns > 0:

    user_guess = int(input("What is your guess? > "))

    if user_guess == number:
        print("Wow! You're amazing! How did you get the answer so quickly?")
        correct = True
        break
    elif user_guess > number:
        turns = turns - 1
        print(f"Too high. You have {turns} guesses left ")
    elif user_guess < number:
        turns = turns - 1
        print(f"Too low. You have {turns} guesses left ")
    else:
        print("Error")
        break

print(f"""

The number was {number},
Better luck next time {username}!

""")
