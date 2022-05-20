from pandas import DataFrame as df
import pandas as pd
import numpy as np

    #Création du tableau
tableau=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(tableau)

    #Selectionner des colonnes et des lignes
#CONTENU D'UNE CELLULE
#Afficher la 2e lignes de la 3e colonne 
print(tableau.iloc[1,2]) 

#CONTENU DE PLUSIEURS CELLULES
#Afficher la 1er à la 3 ln, 1er à la 3e cln 
print(tableau.iloc[0:2, 0:2]) 
#Afficher les 2 premières lignes du tableau
print(tableau.iloc[0:2,:])
print(tableau.iloc[0:2,0:3])
 
#iloc = indice de localisation 
#loc = le nom du contenu 

#Afficher les lignes par position
tableau.head(2) #Afficher les 2 premières lignes

#Donner un nom aux colonnes du tableau
tableau.columns.set_names = ["titre1","titre2","titre3"]
