import random
def plus_moins():
    nb= -1
    nb_deviner = random.randint(0, 9)
    while nb != nb_deviner:
        nb = int(input("choisir un nb entre 0 et 9?"))
        if nb > nb_deviner:
            print("C'est moins.")
        elif nb < nb_deviner:
            print("C'est plus.")
        else:
            print("T'as réussi !")

plus_moins()