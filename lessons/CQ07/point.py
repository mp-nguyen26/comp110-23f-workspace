"""yeah."""

class Point:

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int):
        self.x += factor
        self.y += factor

    