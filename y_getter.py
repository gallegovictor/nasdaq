import os
import pandas as pd
import numpy as np 
from MyUtils import * 

import random

df = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/X.csv')
df = df.drop(df.columns[0], axis=1)
print(df.columns)
w_prueba = np.random.uniform(size=90) 
w_prueba = w_prueba/sum(w_prueba)
y = df.dot(w_prueba)


y.to_csv('/home/victor/Documentos/GitHub/nasdaq/y.csv')
print(y)

#w_list = MyUtils.solver(df,y)