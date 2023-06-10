import pandas as pd 
import numpy as np
from MyUtils import * 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pickle 
X = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/2_weeks_training/X_best_columns_2W_74.csv')
y = pd.read_csv('y.csv')
y = y.drop(y.columns[0], axis=1)
X = X.drop(X.columns[0], axis=1)
#extra = pd.DataFrame(pd.read_csv('X.csv').drop(pd.read_csv('X.csv').columns[:4],axis=1).sum(axis=1))
print(X.columns)
print(y.head())
print("X shape:", X.shape)
print("y shape:", y.shape)
weights = MyUtils.solver(X,y)
reg = LinearRegression().fit(X[:124], y[:124])

optimal_score = reg.score(X[125:149], y[125:149])
print("Score: ", optimal_score)
print("Intercept before: ",reg.intercept_)
print("Weights before: ", reg.coef_)
reg.coef_ = weights.ravel()
reg.intercept_ = 0
solver_score =reg.score(X[125:149], y[125:149])
print("Score: ", solver_score)
print("Intercept after: ",reg.intercept_)
print("Weights after: ", reg.coef_)
iters = int(X.shape[0]/100)
score_list = []
total_avg_score = []
total_avg_var = []


for i in range(0,iters):

        
    temp = X
    #X = X.drop(X.columns[-1], axis=1)
    start= MyUtils.WEEKLY_SAMPLES*i*2
    finish = (MyUtils.WEEKLY_SAMPLES*i*2+MyUtils.WEEKLY_SAMPLES)
    test_start = (MyUtils.WEEKLY_SAMPLES*i*2+MyUtils.WEEKLY_SAMPLES+1)
    test_finish = (MyUtils.WEEKLY_SAMPLES*i*2+MyUtils.WEEKLY_SAMPLES+1+MyUtils.WEEKLY_SAMPLES)
    reg = LinearRegression().fit(temp[start:finish], y[start:finish])
    print("Score using days from: " + str(start) +"to" +str(finish))
    reg.coef_ = weights.ravel()
    reg.intercept_ = 0
    score = reg.score(temp[test_start:test_finish], y[test_start:test_finish])
    print("Score:", score)
    score_list.append(score)
    #print("Average score: so far", avg)
    if test_finish > temp.shape[0]:
        break
    avg = np.mean((np.array(score_list)))
    var = np.var((np.array(score_list)))
    print("Average score in iter #:", avg)
    print("Variance:  ", var)
    total_avg_score.append(avg)
    total_avg_var.append(var)

print("Overall var ",total_avg_var )
print("\n\nOverall score", total_avg_score)


####Testing random columns
score_dict = {}
random_score_list = []
solvers_list = []
# X_big = pd.read_csv('/home/victor/Documentos/GitHub/TFG/X.csv')
# X_big = X_big.drop(X_big.columns[:4], axis=1)

full_score_list = []
full_total_avg_score = []
full_total_avg_var = []

#print(X_big)
full_weights = MyUtils.solver(X, y)

print(np.array(total_avg_score).mean())

# print(MyUtils.get_nth_combination(X_big.columns, 19,0))
# print(MyUtils.get_nth_combination(X_big.columns, 19,1236))

col_set = []
#print(X_big)
for i in range(0,100):
    if i % 2 == 0:
        cols = MyUtils.get_nth_combination(X.columns,16,i*1000)
    else: 
        cols = MyUtils.get_nth_combination(X.columns,16,(1000000-i))
    X_random = X.loc[:,cols]
    print(X_random.columns)
    random_weights = MyUtils.solver(X_random, y)
    for j in range(0,iters):
        temp = X_random
        #X = X.drop(X.columns[-1], axis=1)
        start= MyUtils.WEEKLY_SAMPLES*j*3
        finish = (MyUtils.WEEKLY_SAMPLES*j*3+MyUtils.WEEKLY_SAMPLES)
        test_start = (MyUtils.WEEKLY_SAMPLES*j*3+MyUtils.WEEKLY_SAMPLES+1)
        test_finish = (MyUtils.WEEKLY_SAMPLES*j*3+MyUtils.WEEKLY_SAMPLES+1+MyUtils.WEEKLY_SAMPLES)
        random_reg = LinearRegression().fit(temp[start:finish], y[start:finish])
        print("Score using days from: " + str(start) +"to" +str(finish))
        random_reg.coef_ = random_weights.ravel()
        random_reg.intercept_ = 0
        score = random_reg.score(temp[test_start:test_finish], y[test_start:test_finish])
        print("Score:", score)
        random_score_list.append(score)
        #print("Average score: so far", avg)
        if test_finish > temp.shape[0]:
            break
        rnd_avg = np.mean((np.array(score_list)))
        rnd_var = np.var((np.array(score_list)))
        print("Average score in iter #:", rnd_avg)
        print("Variance:  ", rnd_var)

    score_dict.update({cols:np.array(random_score_list).mean() })
    col_set.append(cols)
print(score_dict.values())
print(col_set)

#Primera conclusión, el método de elegir con cariño es mejor que elegir por azar 

##Meter aquíplot para ver puntuaciones 

# plt.bar(range(len(score_dict)), list(score_dict.values()), align='center')
# plt.xticks(range(len(score_dict)), list(score_dict.keys()))
# plt.bar(1, total_avg_score, label='Best solution obtained', color='r')
# #plt.xticks(range(len(X.columns)), list(score_dict.keys()))
# plt.yticks([(i)/20 for i in range(21)]) 
# plt.ylim(top=np.max(np.array(total_avg_score)))
# plt.savefig('/home/victor/Documentos/GitHub/TFG/2_weeks_training/19col_2weeks_plot.jpg')
# plt.show()
#repetir resto para guardar histogramas 
# Store data (serialize)
mean_score  = np.mean(np.array(total_avg_score))
with open('/home/victor/Documentos/GitHub/nasdaq/2_weeks_training/2W_74_random.pickle', 'wb') as handle:
    pickle.dump(score_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('/home/victor/Documentos/GitHub/nasdaq/2_weeks_training/2W_74_score.pickle', 'wb') as handle:
    pickle.dump(mean_score, handle, protocol=pickle.HIGHEST_PROTOCOL)
