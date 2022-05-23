import pandas as pd
from pandas import read_csv


# Nous importons tout d'abord nos données
data = pd.read_csv('Abdourahmane\Exercice1.csv', header = 0, index_col= 0, sep=',',decimal='.')
print(data)


prenom = "Abdou"
nom = "Rah"

print("Etudiant : ", prenom," ",nom)

data.sort_values(by=['taille']) #ordonner les données d'un dataframe

print(data.describe())


