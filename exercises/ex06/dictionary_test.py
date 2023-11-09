"""Testing functions from dictionary.py."""

__author__ = "730574011"


from exercises.ex06.dictionary import invert


def test_number_strings() -> None:
    """Tests when the input dictionary has numbers as strings."""
    test_dict: dict[str, str] = {"a": "1", "b": "2", "c": "3"}
    assert invert(test_dict) == {"1": "a", "2": "b", "3": "c"}


def test_different_length_keys_values() -> None:
    """Tests when the input dictionary has keys and values that have different legths."""
    test_dict: dict[str, str] = {"abc": "d", "e": "fgh", "ijk": "l"}
    assert invert(test_dict) == {"d": "abc", "fgh": "e", "l": "ijk"}


def test_empty_dict() -> None:
    """Tests when the input dictionary is empty."""
    assert invert({}) == {}


from exercises.ex06.dictionary import favorite_color


def test_all_same_color() -> None:
    """Tests when the input dictionary has values that are all the same color."""
    test_dict: dict[str, str] = {"Michael": "purple", "Mike": "purple", "Michelle": "purple"}
    assert favorite_color(test_dict) == "purple"


def test_all_different_colors_appear_once() -> None:
    """Tests when the input dictionary has colors that are all unique."""
    test_dict: dict[str, str] = {"Michael": "purple", "Mike": "blue", "Michelle": "red"}
    assert favorite_color(test_dict) == "purple"


def test_empty_dict() -> None:
    """Tests when the input dictionary is empty."""
    assert invert({}) == {}


from exercises.ex06.dictionary import count


def test_number_strings() -> None:
    """Tests when the input list has numbers as strings."""
    test_dict: list[str] = ["1", "2", "2", "3", "3", "3"]
    assert count(test_dict) == {"1": 1, "2": 2, "3": 3}


def test_strings_different_length() -> None:
    """Tests when the input list has elements of different lengths."""
    test_list: list[str] = ["a", "ab", "ab", "abc", "abc", "abc"]
    assert count(test_list) == {"a": 1, "ab": 2, "abc": 3}

def test_empty_list() -> None:
    """Tests when the input list is empty."""
    assert count([]) == {}


from exercises.ex06.dictionary import alphabetizer


def test_capital_first_letter() -> None:
    """Tests when the input list has words that start with capital letters."""
    test_list: list[str] = ["Antelope", "Bee", "Cat",]
    assert alphabetizer(test_list) == {"a": ["Antelope"], "b": ["Bee"], "c": ["Cat"]}


def test_same_first_letter() -> None:
    """Tests when the input list has words that all start with the same letter."""
    test_list: list[str] = ["apple", "answer", "ace"]
    assert alphabetizer(test_list) == {"a": ["apple", "answer", "ace"]}


def test_empty_list() -> None:
    """Tests when the input list is empty."""
    assert alphabetizer([]) == {}


from exercises.ex06.dictionary import update_attendance


def test_one_student() -> None:
    """Tests when the original dictionary has only one student for each day."""
    input_dict: dict[str, list[str]] = {"Monday": ["Michael"], "Tuesday": ["Mike"], "Wednesday": ["Michelle"]}
    assert update_attendance(input_dict, "Monday", "Mai") == {"Monday": ["Michael", "Mai"], "Tuesday": ["Mike"], "Wednesday": ["Michelle"]}


def test_new_day() -> None:
    """Tests when a new day is updated to the original attendance."""
    input_dict: dict[str, list[str]] = {"Monday": ["Michael"], "Tuesday": ["Mike"]}
    assert update_attendance(input_dict, "Wednesday", "Mai") == {"Monday": ["Michael"], "Tuesday": ["Mike"], "Wednesday": ["Mai"]}


def test_empty_update() -> None:
    """Tests when the update has no new students or days."""
    input_dict: dict[str, list[str]] = {"Monday": ["Michael", "Mai"], "Tuesday": ["Mike"]}
    assert update_attendance(input_dict, "", "") == {"Monday": ["Michael", "Mai"], "Tuesday": ["Mike"]}
