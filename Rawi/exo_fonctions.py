import pandas as pd
from pandas import read_csv

#-------------------------TABLEAU-------------------------

data = pd.read_csv('Exercice1.csv', header=0 ,index_col=0 , sep=',' , decimal='.')
data.sort_values(by=["age"])    # Ordonne la data par l'age
print(data)
print (data.describe())         #Desc de la table data
data.sort_values(by=["age"])

#---------------------------------------------------------

prenom = "Rawi"
age = 19
print (prenom, "à", age, "ans.")

#---------------------------------------------------------