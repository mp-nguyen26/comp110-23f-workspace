"""File to define Bear class."""

class Bear:

    age: int
    hunger_score: int
    
    def __init__(self):
        """Constructor."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        self.age += 1
        return None