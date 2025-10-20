import json

def save_grid(grid, filename="grid_save.json"):
    with open(filename, "w") as file:
        json.dump(grid, file)
        
def save_turn(turn, filename="turn_save.json"):
    with open(filename, "w") as file:
        json.dump(turn, file)
        
