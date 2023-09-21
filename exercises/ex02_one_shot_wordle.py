"""Wordle but with only one try ;)"""

__author__ = 730574011

secret: str = ("python")
guess: str = input("What is your 6-letter guess? ")
guess_idx: int = 0
result: str = ("")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
while len(guess) != len(secret):
    guess: str = input("That was not 6 letters! Try again: ")
if len(guess) == len(secret):
    while guess_idx < len(guess):
        if guess[guess_idx] == secret[guess_idx]:
            result += GREEN_BOX
        else:
            other_matches: bool = False 
            secret_idx_check: int = 0
            while other_matches == False and secret_idx_check < len(secret):
                if secret[secret_idx_check] == guess[guess_idx]:
                    other_matches: bool = True
                else:
                    secret_idx_check += 1
            if other_matches == True:
                result += YELLOW_BOX
            else:
                result+= WHITE_BOX
        guess_idx += 1
    print(result)
    if guess == secret:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")
    exit()

   




   


