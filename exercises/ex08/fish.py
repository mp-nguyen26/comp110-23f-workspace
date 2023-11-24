"""File to define Fish class."""

__author__ = "730574011"


class Fish:
    """Defining Fish class."""
    age: int

    def __init__(self):
        """Initializing."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Aging fishes by one day."""
        self.age += 1