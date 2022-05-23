import pandas as pd
from pandas import DataFrame as df

import numpy as np

#dataframe -> gros gros tableau de donnée

tableau = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]))
print(tableau)

"""
print(tableau.iloc[1,2]) #iloc découpe des parties du tableau
#il faut écrire print 

print(tableau.iloc[0:2,0:2])

print(tableau.iloc[0:2,0:3]) #on veut les deux premieres lignes et les 3 premieres colonnes du tableau

#Affichons les 2 premières lignes du tableau
ligne_1_2 = tableau.head(2) 
print(ligne_1_2)
"""


# Nous allons tester de nouvelles colonnes

print()

print(tableau.index) # Noms des lignes
print()

print(tableau.columns) # Noms des colonnes
print()

print(tableau.dtypes) # Types de données du tableau
print()

tableau.columns.__str__().lower # Passer le contenu en minuscules
print()

df.columns.__str__().upper() # Passer le contenu en majuscules
print()

print(tableau.size) # Quantité d'informations contenues dans le tableau
print()

print(tableau.shape) # Dimensions (Nombre de lignes et colonnes)
print()

