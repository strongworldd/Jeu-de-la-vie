import os
import time
from cell_state import next_generation
from loop_detection import detect_loop
from create_grid import create_grid, printgrid 
from load_state import load_grid, load_turn
from save_state import save_grid, save_turn

def main():
    while True:
        reload = input("Do you want to load a saved grid? (y/n): ").strip().lower()
        if reload == 'y':
            grid = load_grid()
            turn = load_turn()
            time.sleep(1.5)
            if grid is False:
                print("This grid is stuck on a loop. Creating a new grid instead.")
                grid = create_grid()
                turn = 0
            elif grid or turn is None:
                print("The grid or the number of turns hasn't been saved. Creating a new grid instead.")
                grid = create_grid()
                turn = 0
            break
        elif reload == 'n':
            print("You chose to not load a saved grid. Creating a new grid instead.")
            grid = create_grid()
            turn = 0
            break
        else :
            print("Invalid input. Please retry.")
            
    seen = {}
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"{turn}")
        printgrid(grid)

        loop, start, period = detect_loop(seen, grid, turn)
        
        if loop:
            if any(1 in ligne for ligne in grid)==False:
                print(f"Everything is dead at turn {start}. Simulation ended.")
            else:
                print(f"Loop detected! Start at turn {start}, period = {period} turns")
            save_grid(False)
            break  

        grid = next_generation(grid)
        turn += 1
        
        save_grid(grid)
        save_turn(turn)

        time.sleep(0.2)
        

if __name__ == "__main__":
    main()
