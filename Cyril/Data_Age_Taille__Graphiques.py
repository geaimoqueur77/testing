import matplotlib.pyplot as plt
import pandas as pd

# matplotlib.use("Qt5Agg")

data = pd.read_csv('../../../Exo_Python/3_Exploration_données/Données.csv', sep=',', decimal=".")
# Importation du fichier de données, avec "," en séparateur, et "." en décimal

x = data.iloc[:, 0]  # Récupère toutes les lignes de la colonne d'index 0 (donc ici l'âge)
y = data.iloc[:, 1]  # Récupère toutes les lignes de la colonne d'index 1 (donc ici la taille)

# --------------------

plt.scatter(x, y, c="green")  # Nuage de points de y (taille) en fonction de x (âge). Points de couleur verte
plt.xlabel('âge')  # Label de l'abscisse
plt.ylabel('taille')  # Label de l'ordonnée
plt.grid(True)  # Tracé d'un quadrillage
plt.show()  # Fonction obligatoire pour afficher le graphique.
# Jusque là, ce n'était que de l'initialisation des différents paramètres

# --------------------

plt.bar(x, y, color="green")  # Diagramme à barres
plt.xlabel('âge')
plt.ylabel('taille')
plt.grid(True)
plt.show()

# --------------------

plt.hist(x, bins=5, color="green")  # Histogramme
plt.xlabel('âge')
plt.ylabel('taille')
plt.grid(True)
plt.show()

# --------------------

plt.plot(x, y, color="green")  # Courbe reliant les points (sans les points
plt.xlabel('âge')
plt.ylabel('taille')
plt.grid(True)
plt.show()
