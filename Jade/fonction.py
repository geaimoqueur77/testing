from pydoc import describe
from pandas import read_csv
import pandas as pd 

#importer un jeu de donnée
data= pd.read_csv('C:/Users/Yvan/Documents/MIASHS/stage/Exercice1.csv', header =  0,index_col=0, sep=',', decimal='.' )
print(data)

print("GO LES MIAHS")

prenom = "Jade"
print(prenom)

nom = "Sandre"
print(nom)

print("Directeur de l'UFR:",prenom,nom)

#visualiser les donnée
data.sort_values(by = ['taille'])# Ordonner les données d'un dataframe
print(data)
data.describe()# Equivalent à summary() en R : résume les données



