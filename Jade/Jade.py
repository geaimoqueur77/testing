jade = list() #creer la liste
print(jade) #montrer la liste

jade.append ("dodo") #ajouter un element à la liste
print(jade)

repas = ["fruit", "legume"] # Liste de mots
repas = [1, 2, 3] # Liste de chiffres
nutrition = [20, "mangue", 3, "banane"] # Liste mixte
activite = list(range(19)) # Liste de chiffres de 0 à 19
act = list(range (0,20,1))
print(act)
ville = list(range(1, 10, 2)) # Liste de chiffres de 1 à 10 en allant de 2 en 2
print(repas)
print(nutrition)
print(activite)
print(ville)

print(len(act)) #longeur de la lste
act[19]


nouvelle = ["dino", 3]
print(nouvelle)
deuxieme = ["pancake"]
print(deuxieme)

MegaListe = [nouvelle, deuxieme] #lier les deux listes
print(MegaListe)

element = MegaListe[0][1] #voir la 1e liste le 1e element
print(element)

chiffre = [3,2,1]
print(chiffre)

chiffre.sort() #trier les chiffres (1,2,3)
print(chiffre)

nouvelle.pop (0) #supprime le mot dino
print(nouvelle)