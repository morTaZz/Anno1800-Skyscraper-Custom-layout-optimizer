import math

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class PrintCoordinate:
    def __init__(self, x, y, print_char):
        self.coordinate = Coordinate(x, y)
        self.print_char = print_char

    def is_same_coordinate(self, x, y):
        return self.coordinate.x == x and self.coordinate.y == y