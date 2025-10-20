import os
import time
from cell_state import next_generation
from loop_detection import detect_loop
from create_grid import create_grid, printgrid 
from load_grid import load_grid
from savestate import save_grid

def main():
    while True:
        reload = input("Do you want to load a saved grid? (y/n): ").strip().lower()
        if reload == 'y':
            grid = load_grid()
            time.sleep(1.5)
            if grid is False:
                print("This grid is stuck on a loop. Creating a new grid instead.")
                grid = create_grid()
            elif grid is None:
                print("No grid has been saved. Creating a new grid instead.")
                grid = create_grid()
            break
        elif reload == 'n':
            print("You chose to not load a saved grid. Creating a new grid instead.")
            grid = create_grid()
            break
        else :
            print("Invalid input. Please retry.")
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
            save_grid(False)
            break  

        grid = next_generation(grid)
        turn += 1
        
        save_grid(grid)

        time.sleep(0.2)
        

if __name__ == "__main__":
    main()
