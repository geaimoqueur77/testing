import pandas as pd
import numpy as np

tableau= pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(tableau,"\n")
print("acceder à la premier ligne deuxieme colonne:\n",tableau.iloc[1,2],"\n")#acceder à la premier ligne deuxieme colonne
print(tableau.iloc[0:2,0:2],"\n")#acceder à 1 2 et 4 5 
print("acceder aux deux premieres lignes:\n",tableau.iloc[0:2,:],"\n")#acceder aux deux premieres lignes
print("autre methode:\n",tableau.head(2))#autre méthode pour acceder aux deux premieres lignes 


print(tableau.index)
#print(tableau.dtype)
print(tableau.size )# Quantité d'informations contenues dans le tableau
print(tableau.shape) # Dimensions (Nombre de lignes et colonnes)


#print(tableau.factorize()) # Obtenir une liste des modalités de la variable (similaire SELECT DISTINCT en SQL)
#print(tableau.to_numeric()) # Convertir en nombre (similaire à inttostr() en Pascal)
#print(tableau.astype(NomType)) # Convertir en type de variable à préciser
#print(tableau.copy() )# Pe

tableau.columns.set_names=["lolo","momo","soso"]
print(tableau.columns)