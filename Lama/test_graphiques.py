import pandas as pd 
from pandas import read_csv 
data=pd.read_csv('C:\\Users\\Lama\MonProjet\\Exercice1.csv', header=0, index_col=0 , sep=',' , decimal='.')
print(data)




#-------------------#


from matplotlib import pyplot as plt
plt.plot(data, color='yellow', linestyle = ':',marker = 'o', markersize = 10) # Créer une courbe
plt.ylabel('taille')
plt.xlabel('age')
plt.title('Courbe des ages et tailles')
plt.grid(True)
plt.show() #Afficher la courbe

#--------------------#


plt.hist(data, bins = 5, color = 'skyblue') # Créer un histogramme
plt.ylabel('taille')
plt.xlabel('age')
plt.title('Histogramme des ages et tailles')
plt.show() # Afficher un histogramme




