import random
def jeu():
    nb= -1
    nb_deviné = random.randint(1, 11)
    while nb != nb_deviné:
        print("choisir un nb entre 1 et 9?")
        nb = int(input())
        if nb > nb_deviné:
            print("C'est moins.")
        elif nb < nb_deviné:
            print("C'est plus.")
        else:
            print("T'as réussi !")

jeu()