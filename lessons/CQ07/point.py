"""Defining methods for a new class called Point."""

from __future__ import annotations


class Point:
    """Defining attributes of class Point."""

    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int):
        """Modifies point by multiplication with a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates new point by multiplication with a factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Makes printed point readable."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Another way to implement scale using mult operator overload."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Addition operator overload."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point