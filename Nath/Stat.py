import pandas as pd
from pandas import read_csv
import numpy as np

    
donnees=pd.read_csv('C:\\Users\\33669\\Documents\\testing\\Nath\\Exercice1.csv', header=0,sep=',', decimal='.')
print(donnees)
print(donnees.columns)

#somme par colonne
print(np.sum(donnees))

#moyenne de chaque colonne
print(np.mean(donnees))

#médiane de chaque colonne
print(np.median(donnees))

#ecart-type de chaque colonne
print(np.std(donnees))

#quintille de chaque colonne, le 2e paramètre désigne la quantité voulue
#Ici 25%, Q1
print(np.percentile(donnees,25))

#Resume de toutes les donnees statistiques du jeu de donnees
print(donnees.describe())


