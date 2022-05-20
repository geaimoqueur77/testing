#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:24:15 2022

@author: antoinesedoh
"""
#On créee une liste nommée NomListe
NomListe = list()

# On y  rajoute "3"
NomListe.append(3)


liste1= ["dinosaure", "pancakes"] # Liste de mots
liste2= [1, 2, 3] # Liste de chiffres
liste3= [17, "pirouette", 3, "cacahouète"] # Liste mixte

#On crée une liste de liste avec les liste 1, 2 et 3. 
MegaListe = [liste1, liste2, liste3]

#On affiche le contenu de la liste
print ("Le contenu de la liste est : ",liste1)
print ("Le contenu de la liste est : ",liste2)
print ("Le contenu de la liste est : ", liste3)


#Pour pouvoir aérer l'affichage
print("")
print("")

# On affiche la longueur de la liste
print ("La longueur de la liste est : ", len(liste1))
print ("La longueur de la liste est : ", len(liste2))
print ("La longueur de la liste est : ", len(liste3))



print("")
print("")
Element = MegaListe[2][0] #3ème liste, 1er élément (l'index commence à 0)
print("Le premier élément de la troisième liste est : ", Element)

#On trie la liste grâce à la méthode sort ()

liste6 = ["a","d","m", "e", "k", "g"]
print (liste6)
print("")
liste6.sort()
print ("La liste triée est : ", liste6)