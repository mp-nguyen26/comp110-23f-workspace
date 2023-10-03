"""Use this for random stuffs"""

# def f(x: int) -> int:
#     return x
#     x *= 2
#     print(x)

# y: int = f(3)

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
    contains_char(secret, guess[letter_check])
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    result: str = ""
    
    if contains_char is True and guess[letter_check] == secret[letter_check]:
        result += GREEN_BOX
    if True:
        result += YELLOW_BOX 
    if contains_char is False:  
        result += WHITE_BOX
    letter_check += 1