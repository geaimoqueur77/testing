import random
#Exo 0

def puissance (nombre, exposant):
    if nombre >= 1 and nombre <= 10 :
        return (nombre**exposant)
    else : 
        print('le premier nombre doit etre compris entre 1 et 10')

#print(puissance(int(input()), int(input())))
    
#Exo 1

def procedure() : 
    i = False

    while not(i) :
        a = input()
        if a == 'stop' :
            i = True

#procedure()

#Exo 2

def enlever(liste, mot) : 
    motliste = list(mot)
    cmb = len(motliste)
    i = 0
    while i < cmb :
        for j in liste :
            if motliste[i] == j :
                print(motliste[i], 'est compris dans la liste on le supprime')
                motliste[i] = 0
        i += 1
    i = 0
    mot = str()
    for k in motliste :
        if k != 0 :
            mot += k
    print(mot)

voyelle = ['a', 'e', 'i', 'o', 'u', 'y']
#enlever(voyelle, input())

#Exo 3

def multiple(nombre, min, max) :
    a = list()
    i = min
    while i <= max :
        if i != 0 :
            if i%nombre == 0 :
                a.append(i)

        i += 1

    print(a)

#multiple(int(input()),int(input()), int(input()) )

#Exo 4


def guess() :
    sol = random.randint(0,9)
    trouve = False
    while not(trouve) : 
        essai = int(input())
        if essai == sol :
            print('trouve !')
            trouve = True
        else :
            if essai < sol :
                print('plus grand !')
            else :
                print('plus petit')

guess()




