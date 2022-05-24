#creer un carre

def carre(n):
    print(n * "-")
    for i in range(n):
        print('|'," " * n,'|')
    print(n * "-")

carre(input("Taille : "))

#a corriger