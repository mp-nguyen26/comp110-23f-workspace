"""Test my zip function."""

__author__ = "730574011"

from lessons.zip import zip


def test_empty_lists() -> None:
    """Tests when lists are empty."""
    assert zip([],[]) == {}


def test_lists_different_length() -> None:
    """Tests when lists are different lenghts."""
    test_list_keys: list[str] = ["A","B","C"]
    test_list_values: list[int] = [1,2]
    assert zip(test_list_keys,test_list_values) == {}


def test_values_list_w_neg() -> None:
    """Tests when the values list has negative numbers"""
    test_list_keys: list[str] = ["A","B","C"]
    test_list_values: list[int] = [-1,2,-3]
    assert zip(test_list_keys,test_list_values) == {"A": -1, "B": 2, "C": -3}