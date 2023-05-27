#from sklearn.linear_model import LinearRegression
import pandas as pd
#import numpy as np
from MyUtils import *

def solver(X,y):
    # y = y[:130]
    # y_sum = y[y.columns[3:]].sum(axis=1)
    #print(y_sum.head())
    r,c = X.shape[0], X.shape[1]
    print('This is r and c: ', r, c)
    G = np.identity(c)
    G = matrix(G*-1)
    A = matrix(np.ones((1,c)), (1,c))
    b = matrix(np.ones((1,1)))


    h = matrix(np.zeros((c,1)))
    alpha = 0.01
    print("This is A:", A.size)
    print("This is G:", G.size)


    # print(X.shape)
    # X_total = []
    # def rtrn(arr, i):
    #     return (arr[i]-arr[i-1])/arr[i-1]

    # for i in range(0,250):
    #     X_total.append(X)
    # return_matrix = []
    # for a in range(0,250):
    #     for b in range(1,26):
    #         return_matrix.append(rtrn(X_total[a], b))
    #X = np.array(X_total)
    #print(return_matrix)


    print(np.isnan(X).any())
    print(X)
    print(np.linalg.matrix_rank(X))
    vol =np.std(np.array(X), 0 ).reshape((1,-1))
    #vol=0.5
    p_matrix = np.dot(np.transpose(X), X) + alpha*vol 
    P = matrix(p_matrix, (c,c))
    print("This is P:", P)
    # print(np.isnan(P).any())
    #print(y.values.shape)
    print(X.shape)
    q = matrix(np.dot(np.transpose(y), X), (c,1))*-1
    print("This is y: ",y)
    print("This is q:", q.size)
    print("This is vol:", vol)
    print("This is b:", b.size)
    # sol =solvers.qp(P, q, G, h,  A, b )

    # Q = 2*matrix([ [2, .5], [.5, 1] ])
    # p = matrix([1.0, 1.0])
    # G = matrix([[-1.0,0.0],[0.0,-1.0]])
    # h = matrix([0.0,0.0])
    # A = matrix([1.0, 1.0], (1,2))
    # b = matrix(1.0)
    sol=solvers.qp(P, q, G, h, A, b)

    print(sol['x'])
    sum =0
    for i in range(0, len(sol['x'])):
        sum+=sol['x'][i]
    print(sum)
    # print(sol['y'])
    # for i in range(0,len(weights)):
    #   result = weights[i] - sol['x'][i]
    #   print("This is the result:\n", result)

    # weights_sol = np.linalg.pinv(X_short).dot(y)
    # print(weights_sol)
    # print(weights)
    # print(len(sol['x']))

    #Ir cambiando alpha por prueba y error
    #Método para quitar columnas a X y vol 
    X[:4]
    print("*******************************************\n\n\n\n\n\n\n\t\tEnd of the function\n\n\n\n\n\n\n*******************************************")
    return np.array(sol['x'])


X = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/X.csv')
y = pd.read_csv('/home/victor/Documentos/GitHub/nasdaq/y.csv')

# np.random.seed(42)
X=X.drop(X.columns[0],axis=1)
y=y.drop(y.columns[0],axis=1)
# # Generate a list of random column names to drop
#columns_to_drop = np.random.choice(X.columns, 30, replace=False)
print(X.shape)
print(y.shape)
# # Drop the randomly selected columns
#X = X.drop(columns_to_drop, axis=1)
# avg_score = []
# for i in range(0,750):
#     lin_reg = LinearRegression().fit(X[:374*i],y[:374*i])
#     score = lin_reg.score(X[375*i:499*i],y[375*i:499*i])
#     print(score)
#     avg_score.append(score)

#print(X.shape)
#print(y.shape)
#Optimization:
solver(X,y)