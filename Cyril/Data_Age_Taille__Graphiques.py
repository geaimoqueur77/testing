import matplotlib.pyplot as plt
import pandas as pd

# matplotlib.use("Qt5Agg")

data = pd.read_csv('../Exo_Python/3_Exploration_données/Données.csv')

x = data.iloc[:, 0]
y = data.iloc[:, 1]

# --------------------

plt.scatter(x, y, color="green")
plt.xlabel('âge')
plt.ylabel('taille')
plt.grid(True)
plt.show()

# --------------------

plt.bar(x, y, color="green")
plt.xlabel('âge')
plt.ylabel('taille')
plt.grid(True)
plt.show()

# --------------------

plt.hist(x, bins = 5, color="green")
plt.xlabel('âge')
plt.ylabel('taille')
plt.grid(True)
plt.show()

# --------------------

plt.plot(x, y, color="green")
plt.xlabel('âge')
plt.ylabel('taille')
plt.grid(True)
plt.show()