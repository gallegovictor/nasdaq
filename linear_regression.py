import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from MyUtils import *
import random 
import matplotlib.pyplot as plt

X = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/X.csv')
y = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/y.csv')
y = y.drop(y.columns[0], axis = 1)
# np.random.seed(42)
# X=X.drop(X.columns[0],axis=1)
# y=y.drop(y.columns[0],axis=1)
# # # Generate a list of random column names to drop
# columns_to_drop = np.random.choice(X.columns, 30, replace=False)
# print(X.shape)
# print(y.shape)
# # Drop the randomly selected columns
# X = X.drop(columns_to_drop, axis=1)
# avg_score = []
# for i in range(0,750):
#     lin_reg = LinearRegression().fit(X[:374*i],y[:374*i])
#     score = lin_reg.score(X[375*i:499*i],y[375*i:499*i])
#     print(score)
#     avg_score.append(score)

# #print(X.shape)
# #print(y.shape)
# #Optimization:
# MyUtils.solver(X,y)


reg = LinearRegression().fit(X[:MyUtils.WEEKLY_SAMPLES], y[:MyUtils.WEEKLY_SAMPLES])
print(reg.score(X[MyUtils.WEEKLY_SAMPLES:(MyUtils.WEEKLY_SAMPLES+MyUtils.DAILY_SAMPLES)], y[MyUtils.WEEKLY_SAMPLES:(MyUtils.WEEKLY_SAMPLES+MyUtils.DAILY_SAMPLES)]))
index_results = []
iters = int(X.shape[0]/100)
print(iters)
first = True
score_list = []
col_dict = {}
save_columns = X.columns
chosen_instruments = np.zeros((100,X.shape[1]))
for a in range(0,100):
  i=0
  for i in range(0,iters):
    if first == True:
      X
      random_numbers = random.sample(range(0, len(X.columns)),43)
      #print(X.columns[list(random_numbers.sort())])
    # Print the random numbers
      print(random_numbers)
      first = False
      temp = X[X.columns[random_numbers]]
    #X = X.drop(X.columns[-1], axis=1)
      print(temp.columns)
    start= MyUtils.WEEKLY_SAMPLES*i*4
    finish = (MyUtils.WEEKLY_SAMPLES*i*4+MyUtils.WEEKLY_SAMPLES)
    test_start = (MyUtils.WEEKLY_SAMPLES*i*4+MyUtils.WEEKLY_SAMPLES+1)
    test_finish = (MyUtils.WEEKLY_SAMPLES*i*4+MyUtils.WEEKLY_SAMPLES+1+MyUtils.WEEKLY_SAMPLES)
    if test_finish > temp.shape[0]:
      print("Broke")
      break
    reg = LinearRegression().fit(temp[start:finish], y[start:finish])
    print("Score using days from: " + str(start) +"to" +str(finish))
    score = reg.score(temp[test_start:test_finish], y[test_start:test_finish])
    
    print("Score:", score)
    if score > 0:
      score_list.append(score)
      
    #index_results.append()
    
    #print("Average score: so far", avg)
  #plt.plot(range(0,len(score_list)), score_list)
  #plt.show()
  avg = np.mean((np.array(score_list)))
  var = np.var((np.array(score_list)))
  
  print("Average score in iter #:" +str(a)+" ", avg)
  print("Variance:  "+str(a)+" ", var)
  for j in range(0,len(temp.columns)):
    print(avg)
    chosen_instruments[a][random_numbers[j]] = avg
    
  first = True
  #print(reg.coef_)
print(np.argsort(sum(chosen_instruments)[::-1]))
col_dict.update({avg:X.columns })

best_columns = X[X.columns[np.argsort(sum(chosen_instruments)[::-1])]]
best_columns = best_columns.drop(best_columns.columns[14:29], axis=1)
x_values = range(len(score_list))


# Create the plot
plt.plot(x_values, score_list, marker='o')
plt.axhline(np.mean(score_list), color='red', linestyle='--')

# Add labels and title
plt.xlabel('Number of scores')
plt.ylabel('R² score')
plt.title('Normalized peak values')
plt.show()
#plt.savefig("nasdaq_normalized.png")
best_columns.to_csv('/home/victor/Documentos/GitHub/nasdaq/4_weeks_training/X_best_columns_4W_43.csv')
# y.to_csv('/home/victor/Documentos/GitHub/TFG/y.csv')
print(MyUtils.solver(X, y))
weights = MyUtils.solver(best_columns, y)
print(weights)