"""In-class CQ 10/17/2023."""

__author__ = "730574011"


def w_sum(float_list: list[float]) -> float:
    """Sums up all values in list using while loop."""
    list_idx: int = 0
    total: float = 0.0
    while list_idx < len(float_list):
        total += float(float_list[list_idx])
        list_idx += 1 
    return total


def f_sum(float_list: list[float]) -> float:
    """Sums up all values in list using for...in...loop."""
    total: float = 0.0
    for values in float_list:
        total += values
    return total


def f_range_sum(float_list: list[float]) -> float:
    """Sums up all values in list using for...in range."""
    total: float = 0.0
    for idx in range(0, len(float_list)):
        values: float = float_list[idx]
        total += values
    return total