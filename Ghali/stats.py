import numpy
from scipy import stats
import pandas as pd
from pandas import read_csv

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

#Mode
print(stats.mode(df))

