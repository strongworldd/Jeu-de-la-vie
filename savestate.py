import json
import os

def save_grid(grid, filename="grid_save.json"):
    with open(filename, "write") as file:
        json.dump(grid, file)
    print(f"✅ Grille sauvegardée dans {filename}")

def load_grid(filename="grid_save.json"):
    if not os.path.exists(filename):
        print("⚠️ Aucun fichier de sauvegarde trouvé.")
        return None
    with open(filename, "read") as file:
        grid = json.load(file)
    print(f"✅ Grille chargée depuis {filename}")
    return grid