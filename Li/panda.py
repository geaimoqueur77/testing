#import
from pandas import DataFrame as df
import panda as pd 

#Par indices
df.iloc[0,5]
df.iloc[0:5,0:3]
df.iloc[:,0:3]
df.loc[:,'NomColonne']

#Par position
df.head(5)
df.head(10)
