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
liste4= range(10) # Liste de chiffres de 0 à 9
liste5= range(1, 10, 2) # Liste de chiffres de 1 à 10 en allant de 2 en 2

#On crée une liste de liste avec les liste 1, 2 et 3. 
MegaListe = [liste1, liste2, liste3]

#On affiche le contenu de la liste
print ("Le contenu de la liste est : ",liste1)
print ("Le contenu de la liste est : ",liste2)
print ("Le contenu de la liste est : ", liste3)
print ("Le contenu de la liste est : ",liste4)
print ("Le contenu de la liste est : ",liste5)

#Pour pouvoir aérer l'affichage
print("")

# On affiche la longueur de la liste
print ("La longueur de la liste est : ", len(liste1))
print ("La longueur de la liste est : ", len(liste2))
print ("La longueur de la liste est : ", len(liste3))
print ("La longueur de la liste est : ", len(liste4))
print ("La longueur de la liste est : ", len(liste5))