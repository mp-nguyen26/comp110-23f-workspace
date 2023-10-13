"""Making functions with lists."""

__author__ = "730574011"


def all(int_list: list[int], the_int: int) -> bool:
    """Checks if all ints of a list matches a specified int."""
    if len(int_list) == 0:
        return False
    else:
        num_of_matches: int = 0
        list_idx: int = 0
        while list_idx < len(int_list):
            if int_list[list_idx] == the_int:
                num_of_matches += 1
            list_idx += 1
        if num_of_matches == len(int_list):
            return True
        else:
            return False


def max(int_list: list[int]) -> int:
    """Returns the max int in a list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        max_int: int = int(int_list[0])
        list_idx: int = 1
        while list_idx < len(int_list):
            if int_list[list_idx] > max_int:
                max_int = int(int_list[list_idx])
            list_idx += 1
        return max_int
    

def is_equal(int_list_1: list[int], int_list_2: list[int]) -> bool:
    """Checks if two int lists are identical."""
    if len(int_list_1) != len(int_list_2):
        return False
    else:
        num_of_matches: int = 0
        list_idx: int = 0
        while list_idx < len(int_list_1):
            if int_list_1[list_idx] == int_list_2[list_idx]:
                num_of_matches += 1
            list_idx += 1
        if num_of_matches == len(int_list_1):
            return True
        else:
            return False