#Introduction Tableaux

from pandas import DataFrame as df
import pandas as pd

import numpy as np

tableau = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(tableau)
print("----------------------")
tab2 = df(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(tab2)
print()

#Localiser des éléments, 2ème ligne 3ème colonne
print(tableau.iloc[1,2])

#Affiche de la première ligne à la deuxième, idem pour les colonnes
print(tableau.iloc[0:2,0:2])
print()

#Affiche les 2 premières lignes et toutes les colonnes, ":" = toutes les lignes/colonnes

#iloc = indice localisation
print(tableau.iloc[0:2,:])
print("------------------------")
print(tableau.iloc[0:2,0:3])
print()

#Affiche les 2 premières lignes
print(tableau.head(2))
print("-----------")

#Affiche toute la colonne d'indice 0
print(tableau.loc[:,0])

#Nb d'éléments au tableau
print(tableau.size)

print(tableau.index)
print(tableau.columns)
print(tableau.dtypes)
print(tableau.shape)

tableau.columns.set_names = ["orange", "kiwi", "fraise"]
print(tableau)

