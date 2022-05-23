from msilib.schema import Directory
from importlib_metadata import csv
import matplotlib as mplt
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("Abdourahmane\Exercice1.csv",header=0, index_col=0,sep=',',decimal='.')

plt.plot(data)
plt.show()

plt.hist(data)
plt.show()
