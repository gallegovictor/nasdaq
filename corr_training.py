import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from MyUtils import * 
from matplotlib import pyplot as plt 

X = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/X.csv')
y = pd.read_csv('y.csv')
y = y.drop(y.columns[0], axis=1)
X = X.drop(X.columns[0], axis=1)

r_dict={}
for j in range(0,74):
  r = np.corrcoef(X[X.columns[j]][:3125],y.values.flatten()[:3125])
  r_dict.update({r[0][1]:X.columns[j]})

print(min(r_dict.values()))
print(min(r_dict.keys()))
print(r_dict.keys())


col_list= MyUtils.get_all_smallest(r_dict,59)

score_list_6m = []
for i in range(0,100):
  if (3125+125*i+374) < 18750:
    reg=LinearRegression().fit(X[col_list][(3125+i*125):(3125+249+i*125)], y[(3125+i*125):(3125+249+i*125)])
    #print(reg.score(X[col_list][(3125+125*i+250):(5574+125*i+374)], y[(5574+125*i+250):(5574+125*i+374)]))
    if reg.score(X[col_list][(3125+125*i+250):(3125+125*i+374)], y[(3125+125*i+250):(3125+125*i+374)])> 0:
        score_list_6m.append(reg.score(X[col_list][(3125+125*i+250):(3125+125*i+374)], y[(3125+125*i+250):(3125+125*i+374)]))
  else: 
    break
print("mean:",np.mean(score_list_6m))
print("std dev:", np.std(score_list_6m))
print(max(score_list_6m))
print(min(score_list_6m))


r_dict_12m={}
for j in range(0,90):
  r = np.corrcoef(X[X.columns[j]][:6250],y.values.flatten()[:6250])
  r_dict_12m.update({r[0][1]:X.columns[j]})

print(min(r_dict_12m.values()))
print(min(r_dict_12m.keys()))
print(r_dict_12m.keys())


score_list_12m = []
for i in range(0,100):
  if (6250+125*i+374) < 18750:
    reg=LinearRegression().fit(X[col_list][(6250+i*125):(6250+249+i*125)], y[(6250+i*125):(6250+249+i*125)])
    #print(reg.score(X[col_list][(2787+125*i+250):(5574+125*i+374)], y[(5574+125*i+250):(5574+125*i+374)]))
    if reg.score(X[col_list][(6250+125*i+250):(6250+125*i+374)], y[(6250+125*i+250):(6250+125*i+374)])>0:
        score_list_12m.append(reg.score(X[col_list][(6250+125*i+250):(6250+125*i+374)], y[(6250+125*i+250):(6250+125*i+374)]))
  else:
    break

print("mean:",np.mean(score_list_12m))
print("std dev:", np.std(score_list_12m))
print(max(score_list_12m))
print(min(score_list_12m))



r_dict_18m={}
for j in range(0,29):
  r = np.corrcoef(X[X.columns[j]][:9350],y.values.flatten()[:9350])
  r_dict_18m.update({r[0][1]:X.columns[j]})

print(min(r_dict_18m.values()))
print(min(r_dict_18m.keys()))
print(r_dict_18m.keys())


score_list_18m = []
for i in range(0,100):
  if (9350+125*i+374) < 18750:
    reg=LinearRegression().fit(X[col_list][(9350+i*125):(9350+249+i*125)], y[(9350+i*125):(9350+249+i*125)])
    #print(reg.score(X[col_list][(2787+125*i+250):(5574+125*i+374)], y[(5574+125*i+250):(5574+125*i+374)]))
    if reg.score(X[col_list][(9350+125*i+250):(9350+125*i+374)], y[(9350+125*i+250):(9350+125*i+374)]) > 0:
        score_list_18m.append(reg.score(X[col_list][(9350+125*i+250):(9350+125*i+374)], y[(9350+125*i+250):(9350+125*i+374)]))
  else:
    break
print("mean:",np.mean(score_list_18m))
print("std dev:", np.std(score_list_18m))
print(max(score_list_18m))
print(min(score_list_18m))

print(len(score_list_12m))
print(len(score_list_18m))
print(len(score_list_6m))

n_list=[]
for i in range(0,63):
  n_list.append(i)

n_list_2=[]
for i in range(0,85):
  n_list_2.append(i)

n_list_3=[]
for i in range(0,86):
  n_list_3.append(i)
# Create a figure and two subplots
fig, ax1 = plt.subplots()

# Create a second axis that shares the same x-axis
ax2 = ax1.twinx()

# Plot the data on the first axis
ax1.plot(n_list_3, score_list_12m, label='12M Score', color='blue')
ax1.set_xlabel('Predictions')
ax1.set_ylabel('Score')

ax1.plot(n_list, score_list_18m, label='18M Score', color='purple')


# Plot the data on the second axis
ax2.plot(n_list_2, score_list_6m, label='6M Score', color='red')


ax1.plot([0,100], [np.mean(score_list_6m),np.mean(score_list_6m)], label='6 months avg', color='green')
ax2.plot([0,100], [np.mean(score_list_12m),np.mean(score_list_12m)], label='12 months avg', color='orange')
ax2.plot([0,100], [np.mean(score_list_18m),np.mean(score_list_18m)], label='18 months avg', color='black')

# Add a legend
ax1.legend(loc='lower left')
ax2.legend(loc='lower right')

# Show the plot
plt.show()
#plt.savefig('/home/victor/Documentos/GitHub/nasdaq/unsupervised_change_basket.png')