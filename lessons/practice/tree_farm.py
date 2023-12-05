"""ChristmasTreeFarm class from QZ03 practice."""

class ChristmasTreeFarm:
    """Represents a christmas tree farm"""
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        """"""
        self.plots: list[int] = []
        idx: int = 0
        while idx < initial_planting:
            self.plots.append(1)
            idx += 1
        while idx < plots:
            self.plots.append(0)

    def plant(self, plot_idx: int):
        """"""
        self.plots[plot_idx] = 1

    def growth(self):
        """"""
        for idx in range(0, len(self.plots)):
            if self.plots[idx] != 0:
                self.plots[idx] += 1

    def harvest(self, replant: bool) -> int:
        """"""
        trees_harvested: int = 0
        if replant is True:
            for idx in range(0, len(self.plots)):
                if self.plots[idx] >= 5:
                    self.plots[idx] = 1
                    trees_harvested += 1
        else:
            for idx in range(0, len(self.plots)):
                if self.plots[idx] >= 5:
                    self.plots[idx] = 0
                    trees_harvested += 1
        return trees_harvested
    
    def __add__(self, new_farm: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """"""
        
