"""Wordle for realsies."""

__author__ = "730574011"


def contains_char(word: str, letter: str) -> bool:
    """Returns true if letter is found in any index of word."""
    assert len(letter) == 1
    letter_idx: int = 0
    while letter_idx < len(word):
        letter_in_word: bool = False
        if letter == word[letter_idx]:
            letter_in_word = True
        else:
            letter_exists_in_word: bool = False 
            current_secret_letter: int = 0
            while letter_exists_in_word is False and current_secret_letter < len(word):
                if letter == word[current_secret_letter]:
                    letter_exists_in_word = True
                current_secret_letter += 1
            if letter_exists_in_word is True:
                letter_in_word = True
            if letter_exists_in_word is False:
                letter_in_word = False
        letter_idx += 1
    return letter_in_word


def emojified(guess: str, secret: str) -> str:
    """Returns green, yellow, or red squares based on position of letter."""
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
    """Checks for correct number of characters."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    game_secret_word: str = "space"
    result: str = ""
    GREEN_BOX: str = "\U0001F7E9"
    while turn_number <= 6 and result != f"{GREEN_BOX}" * len(game_secret_word):
        print(f"=== Turn {turn_number}/6 ===")
        player_guess: str = input_guess(len(game_secret_word))
        print(emojified(player_guess, game_secret_word))
        if player_guess == game_secret_word:
            print(f"You won in {turn_number}/6 turns!")
            turn_number += 7
        else:
            turn_number += 1
    if turn_number == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()