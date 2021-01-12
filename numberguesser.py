from random import *

turns = 10
correct = False
number = randint(1, 1000)

print("""
Welcome to Higher or Lower!
The goal of this game is to
guess a number between 1 and 1000
before you run out of turns

After each guess, you are given
either \"Higher\" or \"Lower\" 
to guide you in the right direction

Use the 'help' command to see a list
of actions
""")

name = input("What is your name? > ")

print(f"""

Welcome to Higher or Lower {name}!

In this game you have {turns} guesses :D

Guess the number correctly within those guesses and you win!

For each wrong guess, you lost a turn, if those turns hit 0, you lose :C
""")

while correct is False and turns > 0:

    user_guess = int(input("What is your guess? > "))

    if user_guess == number:
        print("Wow! You're amazing! How did you get the answer so quickly?")
        correct = True
        break
    elif user_guess > number + 10:
        turns = turns - 1
        print(f"Too high! You have {turns} guesses left :| ")
    elif user_guess < number - 10:
        turns = turns - 1
        print(f"Too low! You have {turns} guesses left :| ")
    elif user_guess > number:
        turns = turns - 1
        print(f"Close, still a little high. You have {turns} guesses left :| ")
    elif user_guess < number:
        turns = turns - 1
        print(f"Close, still a little high. You have {turns} guesses left :| ")
    else:
        print("Error")
        break
