"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730574011"


class Simpy:
    """A class with 1 attribute of list[float]."""

    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, val_list: list[float]):
        """Contructor."""
        self.values = val_list

    def __str__(self) -> str:
        """Magic method for readable output."""
        output: str = f"Simpy({self.values})"
        return output
    
    def fill(self, inp_float: float, inp_int: int) -> None:
        """Method for populating a Simpy with a single float some number of times."""
        self.values = []
        idx: int = 0
        while idx < inp_int:
            self.values.append(inp_float)
            idx += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Method for incrementally populating a Simpy."""
        assert step != 0.0
        current_val = start
        self.values.append(start)
        while stop - step not in self.values:
            current_val += step
            self.values.append(current_val)

    def sum(self) -> float:
        """Method that sums up all values of a Simpy."""
        total: float = sum(self.values)
        return total
    
    def __add__(self, additive: Union[float, Simpy]) -> Simpy:
        """Magic method that adds onto values of a Simpy, takes float or Simpy."""
        new_simpy: Simpy = Simpy([])
        new_simpy = self
        if type(additive) is Simpy: 
            assert len(self.values) == len(additive.values)
            for idx in range(len(self.values)):
                new_simpy.values[idx] += additive.values[idx]
        if type(additive) is float:
            for idx in range(len(self.values)):
                new_simpy.values[idx] += additive
        return new_simpy
    
    def __pow__(self, exponential: Union[float, Simpy]) -> Simpy:
        """Same a previous, but with exponents."""
        new_simpy: Simpy = Simpy([])
        new_simpy = self
        if type(exponential) is Simpy: 
            new_simpy = self
            assert len(self.values) == len(exponential.values)
            for idx in range(len(self.values)):
                new_simpy.values[idx] **= exponential.values[idx]
        if type(exponential) is float:
            for idx in range(len(self.values)):
                new_simpy.values[idx] **= exponential
        return new_simpy
    
    def __eq__(self, other: Union[float, Simpy]) -> list[bool]:
        """Magic method that compares a Simpy's values with another Simpy or float, returns list[bool]."""
        orig_simpy: Simpy = Simpy([])
        orig_simpy = self
        result: list[bool] = []
        if type(other) is Simpy:
            assert len(self.values) == len(other.values)
            for idx in range(len(self.values)):
                if orig_simpy.values[idx] == other.values[idx]:
                    result.append(True)
                else:
                    result.append(False)
        if type(other) is float:
            for idx in range(len(self.values)):
                if self.values[idx] == other:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __gt__(self, other: Union[float, Simpy]) -> list[bool]:
        """Same as previous, but checks if it is greater than original Simpy."""
        orig_simpy: Simpy = Simpy([])
        orig_simpy = self
        result: list[bool] = []
        if type(other) is Simpy:
            assert len(self.values) == len(other.values)
            for idx in range(len(self.values)):
                if orig_simpy.values[idx] > other.values[idx]:
                    result.append(True)
                else:
                    result.append(False)
        if type(other) is float:
            for idx in range(len(self.values)):
                if self.values[idx] > other:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, thing: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Magic method that can filter a Simpy's values."""
        orig_simpy: Simpy = Simpy([])
        orig_simpy = self
        if type(thing) is int:
            result: float = orig_simpy.values[thing]
            return result
        else:
            assert len(orig_simpy.values) == len(thing)
            result: Simpy = Simpy([])
            result = orig_simpy
            simpy_idx: int = 0
            for idx in range(len(orig_simpy.values)):
                if thing[idx] is False:
                    result.values.pop(simpy_idx)
                    simpy_idx -= 1
                simpy_idx += 1

            return result