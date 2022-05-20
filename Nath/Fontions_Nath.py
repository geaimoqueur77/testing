from pydoc import describe
import pandas as pd
from pandas import read_csv
    
    #Importer un jeu de données dans une variable
data=pd.read_csv('Exercice1.csv', header=0, index_col=0,sep=',', decimal='.')
print(data)

    #Pour résumer les données statistiques de jeu de données
print(data.describe()) 

prenom="Nathanaël"
nom="R-R"
age=21
print("Moi je suis:",prenom, nom, age)
