import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('../Exo_Python/3_Exploration_données/Données.csv')

# x = data.iloc[:,0]
# y = data.iloc[:,1]

x = data['age']
y = data['taille']

# ---------- Moyenne ----------

moy_x = np.mean(x)
print(f"Moyenne d'âge : {moy_x}")
# Equivalent à : print("Moyenne d'âge : {} ".format(moy_x))
moy_y = np.mean(y)
print(f"Moyenne de taille : {moy_y}")

# ---------- Variance ----------

var_x = np.var(x)
print(f"Variance de l'âge : {var_x}")
var_y = np.var(y)
print(f"Variance de la taille : {var_y}")
# ---------- Ecart-type ----------

sd_x = np.std(x)
print(f"Ecart-type de l'âge : {sd_x}")
sd_y = np.std(y)
print(f"Ecart-type de la taille : {sd_y}")

# ---------- Médiane ----------

med_x = np.median(x)
print(f"Médiane de l'âge : {med_x}")
med_y = np.median(y)
print(f"Médiane de la taille : {med_y}")

# ---------- Quantiles ----------

Q25_x = np.percentile(x, 25)
print(f"Premier quartile de l'âge : {Q25_x}")
Q25_y = np.percentile(y, 25)
print(f"Premier quartile de la taille : {Q25_y}")

Q75_x = np.percentile(x, 75)
print(f"Troisième quartile de l'âge : {Q75_x}")
Q75_y = np.percentile(y, 75)
print(f"Troisième quartile de la taille : {Q75_y}")

# ---------- Maximum ----------

max_x = max(x)
print(f"Age maximal : {max_x}")
max_y = max(y)
print(f"Taille maximale : {max_y}")

# ---------- Minimum ----------

min_x = min(x)
print(f"Age minimal : {min_x}")
min_y = min(y)
print(f"Taille minimale : {min_y}")

# ---------- Covariance ----------

cov_xx = np.cov(x,y)[0][0]
print(f"Covariance entre l'âge et l'âge : {cov_xx}")
cov_xy = np.cov(x,y)[0][1]
print(f"Covariance entre l'âge et la taille : {cov_xy}")
cov_yx = np.cov(x,y)[1][0]
print(f"Covariance entre la taille et l'âge : {cov_yx}")
cov_yy = np.cov(x,y)[1][1]
print(f"Covariance entre la taille et la taille : {cov_yy}")
mat_cov = np.cov(x,y)
print(f"Matrice de covariance : {mat_cov}")

# ---------- Mode ----------

mode_xy = stats.mode(data)[0]
print(f"Les modes de l'âge puis de la taille sont : {mode_xy}")
mode_freq_xy = stats.mode(data)[1]
print(f"Les modes apparaissent : {mode_freq_xy} fois")
