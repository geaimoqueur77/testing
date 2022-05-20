# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:56:06 2022

@author: HP
"""

from pandas import read_csv
import pandas as pd

data= pd.read_csv("C:/Users/HP/Documents/GitHub/testing/Exercice1.csv", header=0, index_col=0, sep=',',decimal='.') #importation du fichier exercice
print(data)

prenom="Ndeye Fatou"
nom="Dieng"
age='21'
print("Etudiant:",prenom,nom,age)

print(data.describe())#fait le summary , résumé des donnees
print(data.sort_values(by=['taille']))
