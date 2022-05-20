from pandas import read_csv
import pandas as pd

data = pd.read_csv("C:/Users/bourh/OneDrive/Bureau/CoursL3/Stage/Exercice1.csv", header=0, index_col=0, sep=",", decimal=".")
print(data)

prenom = "Dounya"
num = 7
print("Pseudo :", prenom, num)

# Résume les données
print(data.describe())
# Ordonner les données
print(data.sort_values(by=['taille']))
