secret_word = "elephant"
guess = ""
guess_count = 0 # keeps track of how many times the player has guessed
guess_limit = 3 # player has 3 tries
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    # setting a limit on the number of guesses
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, Soz :(")
else:
    print("Yay! You got it!")