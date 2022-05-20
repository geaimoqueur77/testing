#import
from pandas import DataFrame as df
import pandas as pd 


#Par Indices
import numpy as np
tableau = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(tableau)
print(tableau.iloc[1,2])
print(tableau.iloc[0:1,0:1])
print(tableau.iloc[0:2, : ]) #methode 1
print(tableau.iloc[0;2,0:3]) #methode 2

print(tableau.head(1))





