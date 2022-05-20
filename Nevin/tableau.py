#Toujour renommer les importations de librairie avec as

import pandas as pd
import numpy as np
from pandas import DataFrame as df

#tableau =  nom du tableau je peux le changer
tableau = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))

print(tableau)

#print (tableau.iloc[1,2]) # 2 eme ligne 3eme colones
'''''
print(df.iloc(0:2,0:2))
print(tableau.iloc[0:2,0:3])

print(tableau.head(2)) # Afficher les 2 premières lignes
'''''

#print(tableau.index) #Nom des lignes 
#print(tableau.size) nombre d'elements dans le tableau 
print(tableau.shape) #dimensions 3 x 3 

        #Si on ne renomme pas son tableau des noms il attribue des numeros

tableau.colums.set_names = ['Chat','Chien','souris'] 
print(tableau.colums)