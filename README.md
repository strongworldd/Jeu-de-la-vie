Règles
Soit une grille de n lignes et n colonnes
Chaque cellule vaut soit True (vivant) ou False (mort)
A chaque itération les cellules évoluent selon l'état de leurs voisons directs.
Le voisinage considéré est un voisinage de Moore (8 voisins).
Les règles de transition sont fonction de l’état de la cellule et du nombre v de voisins vivants :
si v < 2 l’état suivant est : Mort
si v == 2 la cellule ne change pas d’état
si v == 3 l’état suivant est : Vivant
si v > 3 l’état suivant est : Mort