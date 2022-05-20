#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:48:45 2022

@author: antoinesedoh
"""

from pandas import DataFrame
import pandas as pd
import numpy as np


tableau = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
tableau.columns=['Ligne 1','Ligne 2','Ligne3']
print(tableau)

print("")
print("")
print(tableau.iloc[1,2]) # 2ème ligne, 3ème colonne
print("")
print("")
print(tableau.iloc[0:2,0:2]) # ème ligne, ème colonne

print("")
print("")
# Pour afficher les deux premières lignes et toutes les colonnes.
# En utilisant les index
print(tableau.iloc[0:2,0:3]) 
print("")

# Pour afficher les deux premières lignes et toutes les colonnes.
# En utilisant les index et la virgule
print(tableau.iloc[0:2,: ]) # ème ligne, ème colonne
print("")

# En utilisant la méthode head
print(tableau.head(2)) # ème ligne, ème colonne
print("")


print (tableau.index)# Noms des lignes
print("")
print (tableau.columns) # Noms des colonnes
print("")
print("Le type de données du tableau")
print (tableau.dtypes) # Types de données du tableau
print("")
#print (tableau.columns.str.lower()) # Passer le contenu en minuscules
print("")
#print (tableau.columns.str.upper()) # Passer le contenu en majuscules
print("")
print ("La quantité d'informations contenues est : ",tableau.size) # Quantité d'informations contenues dans le tableau
print("")
print ("La dimension du tableau est : ",tableau.shape) # Dimensions (Nombre de lignes et colonnes)
print("")





