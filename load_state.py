import os
import json

def load_grid(filename="grid_save.json"):
    if not os.path.exists(filename):
        print("⚠️ No saved grid has been found.")
        return None
    with open(filename, "r") as file:
        grid = json.load(file)
    print(f"✅ Grid successfully loaded from {filename}")
    return grid

def load_turn(filename="turn_save.json"):
    if not os.path.exists(filename):
        print("⚠️ No saved number of turns has been found.")
        return None
    with open(filename, "r") as file:
        turn = json.load(file)
    print(f"✅ Number of Turns successfully loaded from {filename}")
    return turn 
    