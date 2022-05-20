from pandas import read_csv
import pandas as pd
data = pd.read_csv('/Users/Yveine/MonProjet/testing/Li/Exercice1.csv',header=0,index_col=0,sep= ',', decimal='.')
print(data)

prenom = "Yufei"
nom = "Li"
print("ETU:",prenom,nom) #ETU: Yufei Li

data.sort_values(by=['taille'])
