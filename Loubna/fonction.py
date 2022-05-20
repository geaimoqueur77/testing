import pandas as pd
from pandas import read_csv

data=pd.read_csv('C:\\Users\\loubn\\Desktop\\tutu\Exercice1.csv', header=0, index_col=0, sep=',', decimal='.')#importer la base
print(data)

prenom="Loubna"
nom="ZIDAN"
print("\n mon nom est:",nom,"\n et mon prenom est :", prenom)

print(data.describe())
print(data.sort_values(by=['age']))# ordonner les ages

