"""Wordle but with only one try ;)!"""

__author__ = "730574011"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
current_guess_letter: int = 0
result: str = ("")

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

while current_guess_letter < len(guess):
    if guess[current_guess_letter] == secret[current_guess_letter]:
        result += GREEN_BOX
    else:
        letter_exists_in_secret: bool = False 
        current_secret_letter: int = 0

        while letter_exists_in_secret is False and current_secret_letter < len(secret):
            if guess[current_guess_letter] == secret[current_secret_letter]:
                letter_exists_in_secret = True
            current_secret_letter += 1
        if letter_exists_in_secret is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

    current_guess_letter += 1

print(result)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
