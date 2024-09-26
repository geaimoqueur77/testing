# =============================================================================
# Fonction : jeu du plus-ou-moins
# =============================================================================
import random as rd


def plus_ou_moins():
    x = str(rd.randint(0, 9))
    c = 1  # Compteur de coups
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    trial = input("Entrez une valeur entre 0 et 9 : ")
    if trial != all(lst):
        trial = input("Entrez une valeur entre 0 et 9 : ")
    while trial != x:
        c += 1
        if trial > x:
            trial = input("Moins")
        elif trial < x:
            trial = input("Plus")
    else:
        print("Gagné en " + str(c) + " coups ! La valeur était " + x)


plus_ou_moins()
