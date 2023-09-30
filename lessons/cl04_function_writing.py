"""Practice writing functions in class 9/26"""

def mimic_letter(my_word: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx + 1 > len(my_word):
        return str("Too high of an index!")
    return str(my_word[letter_idx])

my_word: str = input("Input a word: ")
letter_idx: int = int(input("Input an integer: "))
print(mimic_letter(my_word, letter_idx))
