import pandas as pd
from scipy.stats import shapiro, pearsonr, spearmanr, chi2_contingency, ttest_ind, f_oneway, wilcoxon, mannwhitneyu

data = pd.read_csv("Lucas/Exercice1.csv", header=0, sep=",", decimal=".")
data2 = pd.read_csv("Lucas/Exercice1.csv", header=0, sep=",", decimal=".")
# Test de Shapiro (normalité)
print(shapiro(data))



# Tests de corrélation 


#Pearson : lien d’évolution entre des variables
print(pearsonr(data.age, data.taille))

# Spearman : basé sur les rangs et non les valeurs (bien pour les notes)
print(spearmanr(data.age, data.taille))

# Khi2 : variables qualitatives dépendantes.
print(chi2_contingency(data, data2))



# Tests paramétriques 


# Test de Student : 2 grands échantillons liés
print(ttest_ind(data, data2))


# Test ANOVA : pls grands échantillons liés)
print(f_oneway(data, data2))


#Test non-paramétriques 


# Test Mann-Whitney : distrib de 2 petits échantillons indép
(stat, p) = mannwhitneyu(data, data2)
print(stat, p)
# Test de Wilcoxon  distrib de 2 petits échantillons indépendants en utilisant les rangs
print(wilcoxon(data, data2))