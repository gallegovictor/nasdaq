from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
X = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/X.csv')
y = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/y.csv')

np.random.seed(42)

# Generate a list of random column names to drop
columns_to_drop = np.random.choice(X.columns, 30, replace=False)

# Drop the randomly selected columns
X = X.drop(columns_to_drop, axis=1)
avg_score = []
for i in range(0,750):
    lin_reg = LinearRegression().fit(X[:374*i],y[:374*i])
    score = lin_reg.score(X[375*i:499*i],y[375*i:499*i])
    print(score)
    avg_score.append(score)