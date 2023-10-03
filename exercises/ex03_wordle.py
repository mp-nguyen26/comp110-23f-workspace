"""Wordle for realsies."""

__author__ = "730574011"
def contains_char(word: str, letter: str) -> bool:
    """Returns true if letter is found in any index of word"""
    assert len(letter) == 1
    letter_idx: int = 0
    while letter_idx < len(word):
        if letter == word[letter_idx]:
            return True
        else:
            letter_exists_in_word: bool = False 
            current_secret_letter: int = 0
            while letter_exists_in_word is False and current_secret_letter < len(word):
                if letter == word[current_secret_letter]:
                    letter_exists_in_word = True
                current_secret_letter += 1
            if letter_exists_in_word is True:
                return True
            if letter_exists_in_word is False:
                return False
        letter_idx += 1

def emojified(guess: str, secret: str) -> str:
    """Returns green, yellow, or red squares."""
    assert len(guess) == len(secret)
    letter_check: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    while letter_check < len(secret):     
        if contains_char(secret, guess[letter_check]) is True and guess[letter_check] == secret[letter_check]:
            result += GREEN_BOX
        if contains_char(secret, guess[letter_check]) is True and guess[letter_check] != secret[letter_check]:
            result += YELLOW_BOX 
        if contains_char(secret, guess[letter_check]) is False:  
            result += WHITE_BOX
        letter_check += 1
    return result
        
def input_guess(expected_length: int) -> str:
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess
#     if input
#     guess: str = input(f"What is your {}-letter guess? ")
# current_guess_letter: int = 0
# result: str = ("")

# while len(guess) != len(secret):
#     guess = input(f"That was not {len(secret)} letters! Try again: ")





# WHITE_BOX: str = "\U00002B1C"
# GREEN_BOX: str = "\U0001F7E9"
# YELLOW_BOX: str = "\U0001F7E8"

# secret: str = "python"
# guess: str = input(f"What is your {len(secret)}-letter guess? ")
# current_guess_letter: int = 0
# result: str = ("")

# while len(guess) != len(secret):
#     guess = input(f"That was not {len(secret)} letters! Try again: ")

# while current_guess_letter < len(guess):
#     if guess[current_guess_letter] == secret[current_guess_letter]:
#         result += GREEN_BOX
#     else:
#         letter_exists_in_secret: bool = False 
#         current_secret_letter: int = 0

#         while letter_exists_in_secret is False and current_secret_letter < len(secret):
#             if guess[current_guess_letter] == secret[current_secret_letter]:
#                 letter_exists_in_secret = True
#             current_secret_letter += 1
#         if letter_exists_in_secret is True:
#             result += YELLOW_BOX
#         else:
#             result += WHITE_BOX

#     current_guess_letter += 1

# print(result)

# if guess == secret:
#     print("Woo! You got it!")
# else:
#     print("Not quite. Play again soon!")