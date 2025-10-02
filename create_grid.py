import os
import random

def printgrid(grid):
    for row in grid:
        print("".join("██" if c else "  " for c in row))
    print()

def create_grid():
    
    grid=[]
    
    while True:
        try:
            size = int (input ("Choose the size of the grid (3-50):"))
            if size < 3 or size > 50:
                print ("Invalid Number")
            else:
                break
        except ValueError:
            print ("The size must be an integer")
        
    for _ in range(int(size)):
        grid= [[random.randint(0, 1) for _ in range(int(size))] for _ in range(int(size))]

        os.system("cls" if os.name == "nt" else "clear")
        printgrid(grid)
        
