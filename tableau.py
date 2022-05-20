# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:58:32 2022

@author: HP
"""

from pandas import DataFrame as df
import pandas as pd
import numpy as np

df= pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]])) #creation du tableau
print(df)

print(df.iloc[1,2]) #2eme ligne , 3eme colonne

print(df.iloc[0:2,0:2])#affiche  2 premiere ligne, 2 premiere colonnes

print(df.iloc[0:2,0:3])
print(df.iloc[0:2, :])

print(df.head(2)) #Affiche les 2 premieres lignes


#COMPRENDRE LE CONTENU 

print("Lignes:",df.index)
print("Colonnes:",df.columns)
print("Types:" ,df.dtypes) #tableau de type object
print("En miniscules:",df.columns.__str__().lower())
print(df.size)#quantaite d'informations contenues dans le tableau
print(df.shape)#dimensions du tableau

tableau.columns.set_;names['toto','tata','titi']
