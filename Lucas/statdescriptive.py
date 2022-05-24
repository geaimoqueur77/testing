import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv("Lucas/Exercice1.csv", header=0, sep=",", decimal=".")

print(data.describe())  # Résumer les données

# Somme
print("Somme :", np.sum(data)) 

# Moyenne
print("Moyenne :", np.mean(data.age))

# Médiane
print("Mediane :", np.median(data.age))

# Variance
print("Variance :", np.var(data.age)) 

# Ecart-type
print("Ecart-type: ", np.std(data.age))   

# Quantile
print("Quantile: ", np.percentile(data.age, 10))  

print(stats.mode(data))