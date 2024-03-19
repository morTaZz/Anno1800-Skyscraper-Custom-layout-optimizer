import math
from itertools import product
from UI import GridUI
import tkinter as tk
from Building import Building,Residence
from Coordinate import Coordinate,PrintCoordinate
# Devspace sample push

def calculate_population(residence, all_residences):
    highrise_meta_data = Residence.get_highrise_meta_data(residence.tier)
    panorama_level = calculate_panorama_level(residence, all_residences, highrise_meta_data['radius'])
    return highrise_meta_data['base_population'] + highrise_meta_data['increase_per_level'] * panorama_level

def calculate_panorama_level(center_residence, all_residences, radius):
    panorama_level = center_residence.tier
    for residence in all_residences:
        if residence != center_residence and residence.center_coordinate.distance_to(center_residence.center_coordinate) <= radius:
            if residence.tier < center_residence.tier:
                panorama_level += 1
            else:
                panorama_level += -1
    return max(0, min(5, panorama_level))

def print_layout(residences):
    # Create a list of PrintCoordinate instances for visualization
    print_coordinates = []
    for residence in residences:
        # Mark the residence's center with its tier
        print_coordinates.append(PrintCoordinate(residence.center_coordinate.x, residence.center_coordinate.y, str(residence.tier)))

    # Determine the layout size
    max_x = max([pc.coordinate.x for pc in print_coordinates])
    max_y = max([pc.coordinate.y for pc in print_coordinates])

    # Create a blank layout
    layout = [["X" for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Populate the layout with residences
    for pc in print_coordinates:
        layout[pc.coordinate.y][pc.coordinate.x] = pc.print_char

    # Print the layout
    text = '\n\n'.join([''.join(row) for row in reversed(layout)])
    return text



def main():
    results = []
    outputfile = "Final_layout.txt"
    def on_ui_submit(result): # Function to recieve Building Coordinates from UI
        nonlocal results
        results = result
        root.destroy()

    root = tk.Tk()
    app = GridUI(root, on_ui_submit)  # Pass the callback function to the UI
    root.mainloop()  # Start the Tkinter event loop
    residences = []
    #clear the extra spacing in the results file
    minx = math.inf
    miny = math.inf
    for result in results:
        minx = min(minx,result[0])
        miny = min(miny,result[1])
    newresults = []
    for result in results:
        newresults.append((result[0] - minx,result[1]-miny))

    for xy in newresults:
        residences.append(Residence(Coordinate(xy[0],xy[1]),tier=3))

    mintier = min(residence.tier for residence in residences)


    highscore_population = 0
    highscore_permutation = []

    for permutation in product(range(mintier, 6), repeat=len(residences)):
        for i, tier in enumerate(permutation):
            residences[i].tier = tier
        total_population = sum(calculate_population(r, residences) for r in residences)
        if total_population > highscore_population:
            highscore_population = total_population
            highscore_permutation = permutation
            print(f"Best permutation: {highscore_permutation} with population: {highscore_population}")

    # Update residences to highscore permutation tiers
    for i, tier in enumerate(highscore_permutation):
        residences[i].tier = tier

    print(f"Final permutation: {highscore_permutation} with population: {highscore_population}")
    text = print_layout(residences)
    print(text)

if __name__ == "__main__":
    main()
