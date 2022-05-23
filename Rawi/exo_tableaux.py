#Importation des biblio
from pandas import DataFrame as df
import pandas as pd
import numpy as np

#Création du tableau
tableau = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print (tableau)
print("------------------------------") 
print(tableau.iloc[1,2])                    #affiche la valeur à la 2e ligne 3e col
print("------------------------------")
print(tableau.iloc[0:2,0:2])                #affiche les valeurs des deux premieres lignes et col
print("------------------------------")
print(tableau.iloc[0:2,:])                  #affiche les 2 premieres lignes et toutes les col
print("------------------------------")
print (tableau.head(2))                     #affiche les 2 premieres lignes
print("------------------------------")
tableau.columns.set_names = ['Mangue',"Sushi","Aristo"]