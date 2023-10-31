"""Combining two lists into a dictionary."""

__author__ = "730574011"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Returns a dictionary where the keys are list 1 and values are list 2."""
    if len(keys) == len(values) and len(keys) > 0:
        list_dict = {}
        for idx in range(0, len(keys)):
            list_dict[keys[idx]] = values[idx]
        return list_dict
    else:
        return dict()