import os
import time
from cell_state import next_generation
from loop_detection import detect_loop
from create_grid import create_grid, printgrid 

def main():
    grid = create_grid()
    seen = {}
    turn = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"{turn}")
        printgrid(grid)

        loop, start, period = detect_loop(seen, grid, turn)
        if loop:
            print(f"Boucle détectée ! Début au tour {start}, période = {period} tours")
            break  

        grid = next_generation(grid)
        turn += 1

        time.sleep(0.2)
        

if __name__ == "__main__":
    main()
