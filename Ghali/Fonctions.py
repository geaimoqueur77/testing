import pandas as pd
from pandas import read_csv

#Importer un jeu de données
data = pd.read_csv('Exercice1.csv', header = 0, index_col = 0, sep = ',', decimal = ',')
print(data)

#Tester print
print ("GO LES MIASHS")
prenom = "Ghali"
nom = "El Alami Idrissi"
print ( "My name is : ", nom," , ", nom, prenom)
print ("(ça rend quand même mieux avec James Bond ;( )")

#Gerer les données
data.sort_values(by=['taille'])
print(data)
data.describe()
print(data)
