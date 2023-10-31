"""Quiz 2 odd and even practice."""

def odd_and_even(list1: list[int]) -> list[int]:
   for idx in range(0, len(list1)):
        num: str = list1[idx]
        if idx % 2 == 0 and num % 2 == 1:
            return_list: list[int] = [num]
            return return_list
        else:
            return list()