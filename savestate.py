import json

def save_grid(grid, filename="grid_save.json"):
    with open(filename, "w") as file:
        json.dump(grid, file)