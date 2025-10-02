import os
import random

def afficher(grille):
    for ligne in grille:
        print("".join("█" if c else " " for c in ligne))
    print()

if __name__ == "__main__":
    
    grille=[]
    
    x=input("Choisissez la taille de la grille:")
    for _ in range(int(x)):
        grille= [[random.randint(0, 1) for _ in range(int(x))] for _ in range(int(x))]

        os.system("cls" if os.name == "nt" else "clear")
        afficher(grille)
        
