"""File to define River class."""

__author__ = "730574011"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Definies a River class."""
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fishes older than 3 days, bears older than 5 days."""
        new_fishes: list[Fish] = self.fish
        fish_idx: int = 0
        for fish in self.fish:    
            if fish.age > 3:
                new_fishes.pop(fish_idx)
                fish_idx -= 1
            fish_idx += 1
        self.fish = new_fishes
        new_bears: list[Bear] = self.bears
        bear_idx: int = 0
        for bear in self.bears:
            if bear.age > 5:
                new_bears.pop(bear_idx)
                bear_idx -= 1
            bear_idx += 1
        self.bears = new_bears
        return None

    def bears_eating(self):
        """Bears will eat 3 fish if there are more than 5 fishes."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Removes bear if their hunger score is less than 0."""
        new_bears: list[Bear] = self.bears
        bear_idx: int = 0
        for bear in self.bears:
            if bear.hunger_score < 0:
                new_bears.pop(bear_idx)
                bear_idx -= 1
            bear_idx += 1
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """For every pair of fishes, 4 fishes are born."""
        new_fishes: list[Fish] = self.fish
        baby_fish: int = (len(self.fish) // 2) * 4
        idx: int = 0
        while idx < baby_fish:
            new_fishes.append(Fish)
            idx += 1
        self.fish = new_fishes
        return None
    
    def repopulate_bears(self):
        """For every pair of bears, 1 bear is born."""
        new_bears: list[Bear] = self.bears
        bear_pairs: int = len(self.bears) // 2
        idx: int = 0
        while idx < bear_pairs:
            new_bears.append(Bear)
            idx += 1
        self.bears = new_bears
        return None
    
    def view_river(self):
        """Displays readable population of river."""
        output: str = f"~~~ Day {self.day}: ~~~\n"
        output += f"Fish population: {len(self.fish)}\n"
        output += f"Bear population: {len(self.bears)}" 
        print(output)
        return None
        
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Advances 7 days."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes a specified number of fish."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1