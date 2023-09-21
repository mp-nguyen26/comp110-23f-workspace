"""Wordle but with only one try ;)"""

__author__ = 730574011

secret: str = ("python")
guess: str = input("What is your 6-letter guess? ")
guess_idx: int = 0
result: str = ("")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while guess != secret:
    if len(guess) == 6 and guess != secret:
        while guess_idx < len(guess):
            if guess[guess_idx] == secret[guess_idx]:
                result += GREEN_BOX
            elif guess[guess_idx] == secret[0] or secret[1] or secret[2] or secret[3] or secret[4] or secret[5]:
                result += YELLOW_BOX
            else:
                result+= WHITE_BOX
            guess_idx += 1
        print(result)
        print("Not quite. Play again soon!")
        exit()
    else: 
        guess: str = input("That was not 6 letters! Try again: ")
if guess == secret:
    print("Woo! You got it!")




   


