import numpy as np 
import pandas as pd
from random import seed
from random import random 
from random import *
import MyUtils 
import glob
import re
from itertools import combinations, islice
from cvxopt import matrix, solvers
#from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
class MyUtils:
  PORTFOLIO_PRICE = 10000#USD
  DOW_JONES_PRICE_x10 = 33980.32*10
  WEEKLY_SAMPLES = 5*25-1
  DAILY_SAMPLES = 25
  W_LIST = [2.922516,5.573777,2.996763,3.391957,4.565166,3.046849,0.992112,3.633552,1.845355,0,7.509682,6.185426,0.580025,4.203363,2.838645,1.188727,3.407081,2.614727,0,5.35261,2.528696,1.962813,4.748033,2.066916,2.784041,3.557931,10.047216,4.127545,0.744035,0.793336,0.871903,2.91682]
  for i in range(0, len(W_LIST)):
    W_LIST[i] = W_LIST[i]/100
  
  RES_1 =0
  RES_2 = 10
  RES_3 = 15
  ordered_name_list = ['UNH', 'GS', 'HD','AMGN', 'MCD', 'MSFT', 'CAT', 'HON', 'V', 'CVX', 'TRV', 'JNJ', 'BA', 'CRM', 'AXP', 'AAPL', 'WMT', 'IBM', 'PG', 'JPM', 'MMM', 'NKE', 'MRK', 'DIS', 'KO', 'CSCO', 'WBA', 'VZ', 'INTC']
  ordered_name_list.sort()#Now the list starts at AAPL, AMGN, etc...
  #Samples the dataframe passed as an argument with a resolution of smp minutes, that is
  #RES_1 = 0, 1 sample/ min
  #RES_N = N 1 sample / N min
  def samples(df, smp):
    df =  MyUtils.FillMissingValues(df)
    df= df[["time", "close", "volume"]]
    for i  in range(1,len(df)):
      if df.loc[i,'time'] % (smp-1) != 0:
        df = df.drop(i)
    return df
  #Returns an ordered dictionary of the format DATE:PATH of all the dataframes in 
  #the dataset given in path argument.
  def globPaths(path):
    myDict = {}
    globList = []
    #print(glob.glob(path, recursive=True))
    globList=glob.glob(path, recursive=True)
    for i in range(0, len(globList)-1):
      if '.csv' in globList[i]:
        myDict[(globList[i][-12:-4],globList[i].split('/')[-1][0:-13])] = globList[i]
      else:
        pass
    return dict(sorted(myDict.items()))
    #return globList 
  #Normalize the array passed as an argument so the values sum 1
  def normalize(arr, t_min, t_max):
      norm_arr = []
      diff = t_max - t_min
      diff_arr = max(arr) - min(arr)
      for i in arr:
          temp = (((i - min(arr))*diff)/diff_arr) + t_min
          norm_arr.append(temp)
      return norm_arr
  #Creates a random vector n_random elements
  def random_W(n_random):
    seed(n_random)
    random_vector = [0]*n_random
    for i in range(0,len(random_vector)):
      random_vector[i] = random()
    print(random_vector)
    random_vector = MyUtils.normalize(random_vector, 0.012, 0.052)###Normaliza valores aleatorios para que dé ~1 la suma del vector aleatorio
    print('After normalizing: \n',random_vector)
    result = 0
    for i in range(0,len(random_vector)):
      result = result + random_vector[i] 

    print("The result is:" ,result)##La suma de los valores no es exactamente 1, echarle un ojo...
    return random_vector
  
  def StockReturnsComputing(StockPrice, Rows, Columns):
      StockReturn = np.zeros([Rows-1, Columns])
      for j in range(Columns):        # j: Assets
          for i in range(Rows-1):     # i: Daily Prices
              StockReturn[i,j]=((StockPrice[i+1, j]-StockPrice[i,j])/StockPrice[i+1,j])* 100

      return StockReturn
  #compute daily returns in percentage of the Dow stocks
  def computeDailyReturns(stockPrice, Rows, Cols):  
    stockPriceArray = np.asarray(stockPrice)
    [Rows, Cols]=stockPriceArray.shape
    stockReturns = MyUtils.StockReturnsComputing(stockPriceArray, Rows, Cols)
    print('Daily returns of selective Dow 30 stocks\n', stockReturns)
    return stockReturns

  def meanCovReturns(stockReturns):
    meanReturns = np.mean(stockReturns, axis = 0)
    print('Mean returns of Dow Stocks:\n',  meanReturns)
    covReturns = np.cov(stockReturns, rowvar=False)
    print('Variance-covariance matrix of returns of Dow Stocks:\n')
    print(covReturns)
  
  def computeBeta(dfStock, dfMarket, stockRows, stockColumns, marketRows, marketColumns):
    #extract asset labels of stocks in the portfolio
    assetLabels = dfStock.columns[1:stockColumns+1].tolist()
    print('Portfolio stocks\n', assetLabels)

    #extract asset prices data and market data
    stockData = dfStock.iloc[0:, 1:]
    marketData = dfMarket.iloc[0:, [4]] #closing price 

    #compute asset returns
    arrayStockData = np.asarray(stockData)
    [sRows, sCols]=arrayStockData.shape
    stockReturns = MyUtils.StockReturnsComputing(arrayStockData, sRows, sCols)

    #compute market returns
    arrayMarketData = np.asarray(marketData)
    [mRows, mCols]=arrayMarketData.shape
    marketReturns = MyUtils.StockReturnsComputing(arrayMarketData, mRows, mCols)

    #compute betas of assets in the portfolio
    beta= []
    Var = np.var(marketReturns, ddof =1)
    for i in range(stockColumns):
        CovarMat = np.cov(marketReturns[:,0], stockReturns[:, i ])
        Covar  = CovarMat[1,0]
        beta.append(Covar/Var)
        
        
    #output betas of assets in the portfolio
    print('Asset Betas:  \n')
    for data in beta:
        print('{:9.3f}'.format(data))
    return beta

  def EmptyRowsElimination(dataFrame):

    # read dataset and extract its dimensions
    [Rows, Columns] = dataFrame.shape
    dFrame = dataFrame.iloc[0:Rows, 0:Columns]
    
    # call dropna method from Pandas 
    dFClean = dFrame.dropna(axis =0, how ='all')
    return dFClean

  #function to fill missing values of daily stock prices
  #Mandatory requirements: (1) The dataset should have been cleaned of all empty rows 
  #before missing values are filled, and 
  #(2) the opening row of the dataset should not have any empty fields

  def FillMissingValues(StockPrices):
    
    print('Fill missing values...')
    
    #identify positions of the missing values in StockPrices
    [rows, cols] = np.where(np.asarray(np.isnan(StockPrices)))
    
    #replace missing value with the previous day's price
    for t in range(rows.size):
        i=rows[t]
        j = cols[t]
        if (i-1) >= 0:           
            StockPrices.iloc[i,j]= StockPrices.iloc[i-1, j].copy()
        else:
            print('error')
    return StockPrices
    #Replaces the missing volumes by 1
  def fillMissingVolumes(column):
    return column.replace(np.nan, 1)

  """"
  Returns the name of the instrument
  """
  def getName(path):
    return path.split('/')[7]
  """
  Returns the date with format Y-M-D
  """
  def getDate(path):
    temp = re.findall('\d+', path)
    res = list(map(int, temp))
    return res[1]
  def getNameFromCSV(path):
    return path.split('_')[0]


#Sorts by columns alphabetically
  def sortByColumnsAlpha(df):
    col = df.columns.tolist()
    col.sort()
    for i in range(0, len(col)):
      df[i] = df[col[i]]
    #df.drop[df.columns[:24]]
    return df
  
  
  #Methods used to get price at a certain day and time. 
  #Note that the hour must be between 0 and 25, as it's the dataframe order.
  def priceIndexAt(day, time):
      init_path = '/home/victor/Documentos/GitHub/TFG/clean_dataset'
      total_index = 0
      for name in range(0, len(MyUtils.ordered_name_list)):
        path = init_path + '/' + MyUtils.ordered_name_list[name] + '.US/'
        path = path + str(day)[:4] + '/' + MyUtils.ordered_name_list[name] + '_US_' + str(day) + '.csv'
        df = pd.read_csv(path)
        price=df['close'].values[time]
        n_stocks = int(MyUtils.DOW_JONES_PRICE_x10*MyUtils.W_LIST[name]/price)
        total_index += price*n_stocks
      print("Total index price for that day: ", total_index)
      return total_index
  def priceIndexDaily(day, stock_list):
      init_path = '/home/victor/Documentos/GitHub/TFG/csv_buenos'
      total_index = 0
      first_iter = True
      for i,name in enumerate(MyUtils.ordered_name_list):
        path = init_path + '/' + name + '.US/'
        path = path + str(day)[:4] + '/' +name + '_US_' + str(day) + '.csv'
        df = pd.read_csv(path, index_col=0, header = 0).drop(['volume'], axis=1)
        df.set_index(df['time'], inplace=True, drop=True)
        df = df.drop('time', axis=1)
        print('Reading :' + path ,df.head())
        df.columns = [name]
        if first_iter == True:
          first_iter = False
          first_df = df.copy()
        else:
          first_df = pd.concat([first_df, df], axis=1)
          print(first_df.head())
      return first_df, first_df.dot(stock_list)
    
        
     
  def priceInstrumentAt(day, time, name):
    for i in range(0, len(MyUtils.ordered_name_list)):
      if name == MyUtils.ordered_name_list[i]:
        break
      else:
        pass
    init_path = '/home/victor/Documentos/GitHub/TFG/clean_dataset'
    path = init_path + '/' + name + '.US/'
    path = path + str(day)[:4] + '/' + name + '_US_' + str(day) + '.csv'
    df = pd.read_csv(path)
    price = df['close'].values[time]
    n_stocks = int(MyUtils.DOW_JONES_PRICE_x10*MyUtils.W_LIST[i]/price)
    print('Price for ' + name + ':' + str(n_stocks*price))
    return price*n_stocks


  def add_random_rows(df, n):
    random_rows = df.loc[np.random.choice(df.index, size=n, replace=True)].reset_index(drop=True)
    return pd.concat([df, random_rows])
    
  def get_nth_combination(iterable, r, n):
      """
      Get the nth combination of a given size without repetition.
      
      Arguments:
      iterable -- An iterable (e.g. a list or a string) containing the elements to combine.
      r -- The size of the combinations to generate.
      n -- The index of the combination to get (0-based).
      
      Returns:
      A tuple representing the nth combination of the given size.
      """
      return next(islice(combinations(iterable, r), n, n+1))
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
    #q = matrix(np.dot(np.transpose(y), X), (X.shape[1],1))*-1 
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

  # def best_columns(X, y):
  #   iters = int(X.shape[0]/100)
  #   print(iters)
  #   first = True
  #   score_list = []
  #   col_dict = {}
  #   save_columns = X.columns
  #   chosen_instruments = np.zeros((30,29))
  #   for a in range(0,30):
  #     for i in range(0,iters):
  #       if first == True:
  #         X
  #         random_numbers = random.sample(range(0, len(X.columns)),19)
  #         print(X.columns[random_numbers.sort()])
  #       # Print the random numbers
  #         print(random_numbers)
  #         first = False
  #         temp = X[X.columns[random_numbers]]
  #       #X = X.drop(X.columns[-1], axis=1)
  #         print(temp.columns)
  #       start= MyUtils.WEEKLY_SAMPLES*i*3
  #       finish = (MyUtils.WEEKLY_SAMPLES*i*3+MyUtils.WEEKLY_SAMPLES)
  #       test_start = (MyUtils.WEEKLY_SAMPLES*i*3+MyUtils.WEEKLY_SAMPLES+1)
  #       test_finish = (MyUtils.WEEKLY_SAMPLES*i*3+MyUtils.WEEKLY_SAMPLES+1+MyUtils.WEEKLY_SAMPLES)
  #       reg = LinearRegression().fit(temp[start:finish], y_df[start:finish])
  #       print("Score using days from: " + str(start) +"to" +str(finish))
  #       score = reg.score(temp[test_start:test_finish], y_df[test_start:test_finish])
  #       print("Score:", score)
  #       score_list.append(score)
  #       #print("Average score: so far", avg)
  #       if test_finish > temp.shape[0]:
  #         break
  #     avg = np.mean((np.array(score_list)))
  #     var = np.var((np.array(score_list)))
  #     print("Average score in iter #:" +str(a)+" ", avg)
  #     print("Variance:  "+str(a)+" ", var)
  #     for j in range(0,len(temp.columns)):
  #       print(avg)
  #       chosen_instruments[a][random_numbers[j]] = avg
        
  #     first = True
  #     #print(reg.coef_)
  #   print(np.argsort(sum(chosen_instruments)[::-1]))
  #   col_dict.update({avg:X.columns })
  #   return X[X.columns[np.argsort(sum(chosen_instruments)[::-1])]]





  def plot_dict(dictionary, var):
      # Get keys and values from dictionary
      keys = list(dictionary.keys())
      values = list(dictionary.values())
      
      # Plot dictionary values
      plt.plot(keys, values, label='Dictionary Values')
      
      # Plot variable value
      plt.axhline(y=var, color='r', linestyle='--', label='Variable Value')
      
      # Add labels and legend to plot
      plt.xlabel('Keys')
      plt.ylabel('Values')
      plt.title('Dictionary Plot')
      plt.legend()
      
      # Show plot
      plt.show()


  def make_histo(scores_rnd, best_scores, eje):
    eje.hist(scores_rnd, label= 'Random portfolios')
    eje.axvline(np.max(np.array(best_scores)), color='red', lw=2, label = "Optimized portfolio")
    eje.legend()
    #plt.show()


  def get_all_smallest(d, n):
      """
      Get all elements up to the nth smallest element of a dictionary based on the size of the keys.
      :param d: A dictionary
      :param n: The nth smallest element to retrieve (1 for the smallest, 2 for the second smallest, etc.)
      :return: A list of all elements up to the nth smallest element of the dictionary
      """
      sorted_keys = sorted(d.keys())
      if n > len(sorted_keys):
          raise ValueError("n is greater than the number of keys in the dictionary")
      return [d[k] for k in sorted_keys[:n]]