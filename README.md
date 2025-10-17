# Jeu de la Vie — Projet Python

## Règles
- Soit une grille de `n` lignes et `n` colonnes
- Chaque cellule vaut soit `True` (vivant) ou `False` (mort)
- A chaque itération les cellules évoluent selon l'état de leurs voisons directs.
  - Le voisinage considéré est un voisinage de Moore (8 voisins).
- Les règles de transition sont fonction de l’état de la cellule et du nombre `v` de voisins vivants :
  - si `v < 2` l’état suivant est : Mort
  - si `v == 2` la cellule ne change pas d’état
  - si `v == 3` l’état suivant est : Vivant
  - si `v > 3` l’état suivant est : Mort

---

## Fonctionnalités
- **Génération de grille** aléatoire avec une taille choisie par l’utilisateur.  
- **Évolution automatique** à chaque tour avec affichage animé.  
- **Détection de boucles** pour identifier les motifs répétitifs.  
- **Sauvegarde et reprise** d’une partie.

---

## Prérequis
Pour exécuter le projet, vous devez avoir installé sur votre machine :

- **Python 3.8 ou plus récent**
- Aucune bibliothèque externe n’est requise : le projet utilise uniquement la **bibliothèque standard de Python**, y compris le module `json`.

---

## Lancer le programme
1. Ouvrez un terminal dans le dossier du projet  
2. Exécutez la commande :
   ```bash
   python main.py
   
---

## Développeurs du projet
- **Lucas et Kévin**