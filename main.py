import os
import time
from cell_state import next_generation
from loop_detection import detect_loop
from create_grid import create_grid, printgrid 
from load_grid import load_grid
from savestate import save_grid

def main():
    reload = input("Do you want to load a saved grid? (y/n): ").strip().lower()
    if reload == 'y':
        grid = load_grid()
        time.sleep(1.5)
        if grid is None:
            print("No grid has been saved. Creating a new grid instead.")
            grid = create_grid()
    else:
        grid = create_grid()
        
    seen = {}
    turn = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"{turn}")
        printgrid(grid)

        loop, start, period = detect_loop(seen, grid, turn)
        if loop:
            print(f"Loop detected! Start at turn {start}, period = {period} turns")
            break  

        grid = next_generation(grid)
        turn += 1
        
        save_grid(grid)

        time.sleep(0.4)
        

if __name__ == "__main__":
    main()
