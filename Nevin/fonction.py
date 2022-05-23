from telnetlib import NEW_ENVIRON
#from numpy import _NDIterFlagsKind
from pandas import read_csv
import pandas as pd
data = pd.read_csv('C:/Users/nyilmaz/Desktop/Exercice1.csv', header = 0, index_col = 0, sep =',', decimal ='.')
print(data) #Toujours regarder le .csv avant de remplir le header, seq et les decimalee

prenom = "Nevin"
nom ="Yilmaz"
print("Etudiante:", prenom, nom)

#fonction qui affiche toutes les infos moyenne, ecart type etc

print (data.describe()) #sur R c'est summery()

data.sort_values(by='taille') #Par rapport au jeux de données les noms des colones
