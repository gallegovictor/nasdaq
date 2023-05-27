import os
import pandas as pd
import numpy as np 
from MyUtils import * 

import random


rand_nums = np.random.rand(89)

# Append the remaining number that ensures the sum is 1
rand_nums = np.append(rand_nums, 1 - np.sum(rand_nums))

# Verify the sum is 1
#print("Sum:", np.sum(rand_nums))

# Print the generated random numbers
print("Random Numbers:")
print(rand_nums)

df = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/matrix.csv')
df = df.drop(df.columns[0], axis=1)
print(df.head)

for i, col in enumerate(df.columns[:90]):
    df[col] = df[col] * rand_nums[i]

print(df.head)

#df.to_csv('/home/victor/Documentos/GitHub/nasdaq/X.csv')