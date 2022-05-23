#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:55:51 2022

@author: antoinesedoh
"""
from pandas import read_csv
import pandas as pd

#On utilise le parser de csv afin de récupérer nos données dans une variable data
data = read_csv('Exercice1.csv', header = 0, index_col = 0, sep= ',', decimal = '.')
#data = read_csv('https://UrlDuFichierFinissantPar.csv', header = 0, index_col = 0, sep = ';', decimal = ',')
print (data)
print("")


print ("Go les MIASHS")
print("")
prenom = "Antoine"
nom = "SEDOH"
age = 50
print ("L'étudiant",nom ,prenom, "a",age , "ans." )

print("")
print("Le tableau trié par taille décroissante :")
print(data.sort_values(by=['taille'], ascending= False)) # Ordonner les données d'un dataframe
print("")

print("Les statistiques descriptives de notre tableau data : ")
print("")
print (data.describe ()) # Equivalent à summary() en R : résume les données