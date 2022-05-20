"""
Age = 123
Force = 39
Inventaire = {"Poudre de fée":20, "Couteau":1,"écaille de sirène":4}

print("Quel est votre nom ? ")
Nom = input()

print(Nom,", is a Magician ")

"""
#-----calculs
"""
a = 1+1
print(a)


b= a *3
print(b)

c= b/2
print(c)

d= c - 1
print(d)

e = 9%3
print(e)

f = 2**2
print(f)

"""
#-----Liste

Abdou = list()
print(Abdou)

Abdou.append("Lancé d'avion")
print(Abdou)

Abdou.append(9)
print(Abdou)

Dinopod = ["Steakozor","Kebabozorus Rex"]
print(Dinopod)

Notes = [12,4,15,9]
print(Notes)

Mon_age = ["J'ai",20,"ans"]
print(Mon_age)

Compte_19 = list(range(1,20)) #ceci permet de générer une liste rempli de nombres de 1 à 19
print(Compte_19)

compte_0_10 = list(range(0,50,3))
print(compte_0_10)

print(len(compte_0_10))

print(compte_0_10[len(compte_0_10)-1])

print(compte_0_10[-1])

Com_on_veut =["dinosaure",3]
print(Com_on_veut)

pan = ["Vitriole"]
print(pan)

Mega = [Com_on_veut,pan]

print(Mega[0][1]) #ceci nous permet d'accéder aux éléments de la méga liste. On accède à la liste 0 et à sont 1er élément

Nouveliste = [3,2,1]
print(Nouveliste)
Nouveliste.sort() #cette fonction va trier la liste, elle ne renvoie pas de résultat
print(Nouveliste)

Com_on_veut.pop(0) # cette fonction sert à retirer un élément d'une liste
print(Com_on_veut)

