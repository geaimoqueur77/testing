from pandas import DataFrame as df
import pandas as pd
import numpy as np

# Tableau de données
data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print("TABLEAU")
print(data)

"""
# 2ème ligne, 3ème colonne
print(data.iloc[1, 2]);
# 1ère à 2ème ligne et 1ère à 2ème colonne
print(data.iloc[0:2, 0:2])

# 2 premières lignes
print(data.iloc[0:2, 0:3])
print(data.iloc[0:2, :])
print(data.head(2))
"""

print("Index: ", data.index)
print("Nom des colonnes : ", data.columns)
print("Types de données du tableau :\n ", data.dtypes)
print("Passer contenu en minuscule", data.columns.__str__().lower())
print("Passer contenu en minuscule", data.columns.__str__().upper())
print("Quantité d'infos dans le tableau : ", data.size)
print("Dimensions : ", data.shape)



