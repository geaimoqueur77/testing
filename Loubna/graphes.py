import pandas as pd
from pandas import read_csv

data=pd.read_csv('C:\\Users\\loubn\\Desktop\\tutu\Exercice1.csv', header=0, index_col=0, sep=',', decimal='.')#importer la base
print(data)
#----------------------------------
from matplotlib import pyplot as ply
ply.plot(data, color='red', marker='o', markersize=5)
ply.ylabel('taille')
ply.xlabel('age')
ply.title('courbe ages et tailles')
ply.grid(True)
ply.show()
#------------------------------
ply.hist(data, bin=5, color='yellow')
ply.ylabel('taille')
ply.xlabel('age')
ply.title('histogramme ages et tailles')
ply.show()
