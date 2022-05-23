###import
from pandas import DataFrame as df
import pandas as pd 


###Par Indices
import numpy as np
tableau = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(tableau)
tableau.iloc[1,2]
tableau.iloc[0:1,0:1]
tableau.iloc[0:2, : ] #methode 1
tableau.iloc[0:2,0:3] #methode 2
tableau.loc[:,1]
tableau.head(1)


###Comprendre le contenu
tableau.index  #RangeIndex(start=0, stop=3, step=1)
tableau.columns #RangeIndex(start=0, stop=3, step=1)
tableau.dtypes
#0    int64
#1    int64
#2    int64
#dtype: object
tableau.columns.__str__().lower() #'rangeindex(start=0, stop=3, step=1)'
tableau.columns.__str__().upper() #'RANGEINDEX(START=0, STOP=3, STEP=1)'
tableau.size #9
tableau.shape #(3, 3)

###Modifer
tableau.factorize()
tableau.to_numric()





