import numpy
from scipy import stats
import pandas as pd
from pandas import read_csv
from turtle import color
import matplotlib.pyplot as plt

#importation des données
df = pd.read_csv('C:\\Users\\HP\\Desktop\\Exercice1.csv', header = 0, sep = ',', decimal = '.')
#Resumé des données
print(df.describe())

#somme age
print (numpy.sum(df['age']))
#moyenne age
print (numpy.mean(df['age']))
#médiane age
print (numpy.median(df['age']))
#varience age
print (numpy.var(df['age']))
#ecart-type age
print (numpy.std(df['age']))
#quartiles age
print (numpy.percentile(df['age'], 50))


#somme taille
print (numpy.sum(df['taille']))
#moyenne taille
print (numpy.mean(df['taille']))
#médiane taille
print (numpy.median(df['taille']))
#varience taille
print (numpy.var(df['taille']))
#ecart-type taille
print (numpy.std(df['taille']))
#quartiles taille
print (numpy.percentile(df['taille'], 50))


#Mode
print(stats.mode(df))

#Courbe simple
plt.plot(df)
plt.show()

#Histogramme
plt.hist(df)
plt.show()

#Trivial pousuite
plt.pie(df['taille'])
plt.show()

