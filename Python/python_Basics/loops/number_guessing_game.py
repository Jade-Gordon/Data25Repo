# Number guessing game
# Importing is introduced here
import random

"""
1. Random number in a range
2. Capture guess
3. Evaluate user guess
If the user's guess is correct,  we need to state the end of the game.
If the guess is too high/low we need to notify the user.

This is a command-line game, so we'll need some messages for the user so they know what's going on.
A while loop will be used which requires a boolean.

python modules -> https://docs.python.org/3/tutorial/modules.html
"""
game_random_number = random.randint(1, 100)
# print(game_random_number)    # If you run the this multiple times, you'll get a different random number
# We need to notify the user that the game has started:

"""
It's important to capture the guess in the variable.
We'll use this to evaluate if the user's guess was right or not
"""
game_active = True  # to ensure the while loop will run the game once it's started

while game_active:
    game_start_message = "Guess a number between 1 - 100"
    user_guess = int(input())   # cast string to integer
    if user_guess == game_random_number:
        print("You guessed correctly! Yay! :)")
        game_active = False
    elif user_guess < game_random_number:
        print("Too low, guess again!")
    else:
        print("Too high, guess again!")

