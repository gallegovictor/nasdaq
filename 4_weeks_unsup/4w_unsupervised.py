import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from MyUtils import * 
from matplotlib import pyplot as plt 
import pickle
X = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/X.csv')
y = pd.read_csv('y.csv')
y = y.drop(y.columns[0], axis=1)
X = X.drop(X.columns[0], axis=1)




r_dict_2W_14={}
for j in range(0,90):
  r = np.corrcoef(X[X.columns[j]][:2787],y.values.flatten()[:2787])
  r_dict_2W_14.update({r[0][1]:X.columns[j]})

print(min(r_dict_2W_14.values()))
print(min(r_dict_2W_14.keys()))
print(r_dict_2W_14.keys())

col_list_2W_43 = MyUtils.get_all_smallest(r_dict_2W_14, 43)

score_list_2W_14 = []
my_weights =[]
for i in range(0,183):
  limit = 6250+125*i+499
  if limit < 18750:
    reg=LinearRegression().fit(X[col_list_2W_43][(6250+i*125):(6250+499+i*125)], y[(6250+i*125):(6250+499+i*125)])
    #print(reg.score(X[col_list][(2787+125*i+250):(5574+125*i+499)], y[(5574+125*i+250):(5574+125*i+499)]))
    my_weights = MyUtils.solver(X[col_list_2W_43][(6250+i*125):(6250+499+i*125)], y[(6250+i*125):(6250+499+i*125)])
    reg.coef_=my_weights.ravel()
    reg.intercept_=0    
    score_list_2W_14.append(reg.score(X[col_list_2W_43][(6250+125*i+250):(6250+125*i+499)], y[(6250+125*i+250):(6250+125*i+499)]))
  else:
    break
print("mean:",np.mean(score_list_2W_14))
print("std dev:", np.std(score_list_2W_14))
print(max(score_list_2W_14))
print(min(score_list_2W_14))
#print(6250+125*i+499)
avg_2w_14_col=np.mean(score_list_2W_14)
print(reg.coef_)

with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_unsup/4W_43_random.pickle', 'wb') as handle:
    pickle.dump(np.mean(score_list_2W_14), handle, protocol=pickle.HIGHEST_PROTOCOL)