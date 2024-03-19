from Coordinate import Coordinate

class Building:
    def __init__(self, center_coordinate=None, size=3):
        self.coordinates = []
        if center_coordinate:
            self.generate_coordinates_for_uneven_square_center(center_coordinate, size)

    def generate_coordinates_for_uneven_square_center(self, center_coordinate, size):
        coordinate_offset = (size - 1) // 2
        x_start = center_coordinate.x - coordinate_offset
        y_start = center_coordinate.y - coordinate_offset

        for x in range(x_start, x_start + size):
            for y in range(y_start, y_start + size):
                self.coordinates.append(Coordinate(x, y))
                
class Residence(Building):
    def __init__(self, center_coordinate, tier=0):
        super().__init__(center_coordinate, size=3)  # Assuming size=3 for simplicity
        self.tier = tier
        self.center_coordinate = center_coordinate

    @staticmethod
    def get_highrise_meta_data(tier):
        highrise_meta_data = {
            1: {'tier': 1, 'cost': 100, 'base_population': 75, 'increase_per_level': 25, 'radius': 4.0},
            2: {'tier': 2, 'cost': 200, 'base_population': 100, 'increase_per_level': 25, 'radius': 4.25},
            3: {'tier': 3, 'cost': 300, 'base_population': 125, 'increase_per_level': 25, 'radius': 5.0},
            4: {'tier': 4, 'cost': 400, 'base_population': 150, 'increase_per_level': 25, 'radius': 6.0},
            5: {'tier': 5, 'cost': 500, 'base_population': 175, 'increase_per_level': 25, 'radius': 6.75},
        }
        if tier not in highrise_meta_data:
            raise ValueError(f"Invalid tier: {tier}. Tier must be between 1 and 5.")
        return highrise_meta_data[tier]