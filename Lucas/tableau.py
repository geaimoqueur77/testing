from pandas import DataFrame as df
import pandas as pd
import numpy as np

df1 = df(np.array(([1,2,3], [4,5,666], [7,8,9])))

#Tableau complet
print()
print(df1) 

# case (2,3)
print()
print(df1.iloc[1,2]) 

#affiche les deux premieres lignes et deux premieres colonnes
print()
print(df1.iloc[0:2,0:2]) 

#Afficher les deux premieres lignes


#Methode 1 
print()
print("Methode 1")
print(df1.iloc[0:2,:])

#Methode 2
print() 
print("Methode 2")
print(df1.iloc[0:2,0:3]) 

#Methode 3
print()
print("Methode 3") 
print(df1.head(2)) 

#Nb de lignes
print()
print(df1.index)

#Nb de colonnes
print(df1.columns)

#Type de données du tableau
print(df1.dtypes)

#Qte d'infos
print(df1.size)

#Dimensiosn
print(df1.shape)

