import os
import pandas as pd
import numpy as np 
from MyUtils import * 

import random

df = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/X.csv')
df = df.drop(df.columns[0], axis=1)
print(df.columns)
y = df.dot(np.ones(df.shape[1]))

y.to_csv('/home/victor/Documentos/GitHub/nasdaq/y.csv')


w_list = MyUtils.solver(df,y)