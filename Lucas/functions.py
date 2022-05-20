from pandas import DataFrame as df
import pandas as pd
import numpy as np

from pandas import read_csv
from pyparsing import col
from sklearn.compose import ColumnTransformer
from sklearn.utils import column_or_1d

#Read csv
data = pd.read_csv('Lucas/Exercice1.csv',header = 0, index_col = 0, sep = ',', decimal = '.')
# Attention au path => La ou vous executer le code, votre programme ne connait pas forcement le fichier

print(data)


prenom = "Lulu"
nom = "la débrouille"
print("Président de la république :", prenom, nom)

data.sort_values(by = ['age'])

print(data.describe())

def Moyenne(arg1, arg2, arg3):
    moyenne = (arg1 + arg2 +arg3)/3

    return moyenne

print(Moyenne(10,18,15))