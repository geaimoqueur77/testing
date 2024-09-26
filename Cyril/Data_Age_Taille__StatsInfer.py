import pandas as pd
from scipy.stats import shapiro, pearsonr, spearmanr, chi2_contingency, ttest_ind, f_oneway, wilcoxon, mannwhitneyu

data = pd.read_csv('../../../Exo_Python/3_Exploration_données/Données.csv')

# x = data.iloc[:,0]
# y = data.iloc[:,1]

x = data['age']     # Ou x = data.age
y = data['taille']  # Ou y = data.taille

# # # Tests de normalité # # #
# ----- Test de Shapiro -----

print(f"Test de Shapiro : {shapiro(data)}")

# # # Tests de corrélation # # #
# ----- Test de Pearson ----- : lien d'évolution entre des variables

print(f"Test de Pearson : {pearsonr(x, y)}")

# ----- Test de Spearman ----- : lien d'évolution entre des variables basé sur les rangs plutôt que les valeurs

print(f"Test de Spearman : {spearmanr(x, y)}")

# ----- Test du Khi2 ----- : variables qualitatives dépendantes

print(f"Test du Khi2 : {chi2_contingency(data, data)}")

# # # Tests paramétriques # # #
# ----- Test de Student ----- : relation entre deux échantillons liés

print(f"Test de Student : {ttest_ind(data, data)}")

# ----- Test ANOVA ----- : relation entre plusieurs échantillons liés

print(f"Test ANOVA : {f_oneway(data, data)}")

# # # Tests non-paramétriques # # #
# ----- Test de Mann-Whitney ----- : distribution de deux petits échantillons indépendants

(stat, p) = mannwhitneyu(data, data)
print(f"Test de Mann-Whitney : {(stat, p)}")

# ----- Test de Wilcoxon ----- : distribution de deux petits échantillons indépendants,
# basé sur leur rang plutôt que leur valeur

print(f"Test de Wilcoxon : {wilcoxon(x,y)}")
