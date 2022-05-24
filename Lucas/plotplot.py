import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Lucas/Exercice1.csv',header = 0, index_col = 0, sep = ',', decimal = '.')

plt.plot(data, "b--", scalex = True, scaley = True)
plt.xlabel('Age', family='serif',color='b',weight='normal', size = 16,labelpad = 6)
plt.ylabel('Taille', family='serif',color='r',weight='normal', size = 16,labelpad = 6)
plt.title("Tailles en fonction de l'age", fontdict={'family': 'serif', 'color' : 'darkblue','weight': 'bold','size': 18})
plt.grid(True)
plt.show()

