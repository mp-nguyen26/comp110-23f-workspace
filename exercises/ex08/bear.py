"""File to define Bear class."""

__author__ = "730574011"


class Bear:
    """Defining class Bear."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Initializing."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        """Aging bears and decrease hunger score per day."""
        self.age += 1
        self.hunger_score -= 1
    
    def eat(self, num_fish: int):
        """Increasing hunger score based on fishes eaten."""
        self.hunger_score += num_fish