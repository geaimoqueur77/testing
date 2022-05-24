from msilib.schema import Directory
from importlib_metadata import csv
import matplotlib as mplt
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("Abdourahmane\Exercice1.csv",header=0,sep=',',decimal='.')
#on peut ajouter "index_col = 0" pour dire que la première colonne numérote les individus

"""
plt.plot(data)
plt.show()

plt.hist(data)
plt.show()

"""
"""
#test de graphiques
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
plt.plot(x,y)
plt.show()

"""


# Partie stats descriptives
# nous allons tester quelques fonctionnalités 

print()
print(data) # on regarde comment s'affichent nos données

print()
dat_fram = pd.DataFrame(data) #fait de nos données une "dataframe"

print()
print(dat_fram) # on veut voir à quoi ressemble la data frame
#La data frame est identique à data créé plus haut

print()
print(dat_fram.describe()) # là on creer une description de nos données que l'on affiche ensuite

print()
print(np.sum(data)) #on cherche ici la somme des donnée avec numpy
#cela nous affiche la somme de chaque colonne

print()
print(np.mean(data))

print() # on va tester pour n'afficher que l'age puis la taille
print(np.mean(data['age']))
print(np.mean(data['taille']))

# print(np.mean(data['age''taille'])) #ceci ne fonctionne guère





