###Creación de vector aleatorio W_rand:
import glob 
import pandas as pd
import os
import numpy as np
from MyUtils import *



 




def globPaths(path):
  myDict = {}
  globList = []
  #print(glob.glob(path, recursive=True))
  globList=glob.glob(path, recursive=True)
  for i in range(0, len(globList)-1):
    myDict[globList[i][-12:-4]] = globList[i]
  return dict(sorted(myDict.items()))

rand_vector = MyUtils.random_W(30)
price_vector = [0]*len(rand_vector)
for i  in range(0, len(price_vector)):
  price_vector[i] = MyUtils.PORTFOLIO_PRICE*rand_vector[i]
#   print("This is the amount of dollars for each instrument in a portfolio of 10000$:\n", price_vector)


dataset_path = '/home/victor/Escritorio/bbdd/**'
pathDict = globPaths(dataset_path)
pathList = {}
for key, value in pathDict.items():
  if '.csv' in value:
    pathList.update({key:value})
  else:
    pass
print(pathList)

# priceDict19 = {"AAPL" : [0]*27*250, "AMGN":[0]*27*250 , "AXP": [0]*27*250, "BA":[0]*27*250, "CAT": 0, "CRM": 0, "CSCO": 0, "CVX": 0, "DIS":0, "DOW":0, "GS":0, "HD":0, "HON": 0, "IBM":0, "INTC": 0, "JNJ":0, "JPM": 0, "KO":0, "MCD":0, "MMM":0, "MRK":0, "MSFT":0, "NKE": 0 , "PG": 0 , "TRV":0, "UNH": 0, "V":0, "VZ":0, "WBA": 0, "WMT":0 }
# priceDict20 = {"AAPL" : 0, "AMGN":0 , "AXP": 0, "BA":0, "CAT": 0, "CRM": 0, "CSCO": 0, "CVX": 0, "DIS":0, "DOW":0, "GS":0, "HD":0, "HON": 0, "IBM":0, "INTC": 0, "JNJ":0, "JPM": 0, "KO":0, "MCD":0, "MMM":0, "MRK":0, "MSFT":0, "NKE": 0 , "PG": 0 , "TRV":0, "UNH": 0, "V":0, "VZ":0, "WBA": 0, "WMT":0 }
# priceDict21 = {"AAPL" : 0, "AMGN":0 , "AXP": 0, "BA":0, "CAT": 0, "CRM": 0, "CSCO": 0, "CVX": 0, "DIS":0, "DOW":0, "GS":0, "HD":0, "HON": 0, "IBM":0, "INTC": 0, "JNJ":0, "JPM": 0, "KO":0, "MCD":0, "MMM":0, "MRK":0, "MSFT":0, "NKE": 0 , "PG": 0 , "TRV":0, "UNH": 0, "V":0, "VZ":0, "WBA": 0, "WMT":0 }
# priceDict22 = {"AAPL" : 0, "AMGN":0 , "AXP": 0, "BA":0, "CAT": 0, "CRM": 0, "CSCO": 0, "CVX": 0, "DIS":0, "DOW":0, "GS":0, "HD":0, "HON": 0, "IBM":0, "INTC": 0, "JNJ":0, "JPM": 0, "KO":0, "MCD":0, "MMM":0, "MRK":0, "MSFT":0, "NKE": 0 , "PG": 0 , "TRV":0, "UNH": 0, "V":0, "VZ":0, "WBA": 0, "WMT":0 }
# for key in priceDict19:
#   priceDict19[key] = [0]*27*250
#   priceDict20[key] = [0]*27*250
#   priceDict21[key] = [0]*27*250
#   priceDict22[key] = [0]*27*250

df=pd.read_csv(list(pathList.values())[0])
##print(df.head) Aquí tengo el dataframe con la ruta del archivo, hay que meterlo en un for...
save_returns_iter = '/home/victor/Escritorio/TFG/returns'
for v in pathList.values():
  print('Iterating thru: '+v)
  df = pd.read_csv(v)
  df = df.drop('Unnamed: 0', axis=1)
  array = np.asarray(df)
  [rows, columns] = array.shape
  returns = MyUtils.computeDailyReturns(array,rows, columns)
  returns = pd.DataFrame(returns, columns=['1', 'close', 'volume'])
  aux_volume = df.drop(['time', 'close'], axis =1)
  df = df.drop(['close', 'volume'], axis=1)
  df = df.join(returns)
  df = df.drop(['1', 'volume'],axis=1)
  df = df.join(aux_volume)
  [n,v_path] = str(v).split("/home/victor/Escritorio/bbdd")
  save_returns_path =save_returns_iter+ v_path
  pd.DataFrame(df).to_csv(save_returns_path)
  #save_path = 
# for key in pathDict:
#   a, b, c ,d = returnPrice(pathDict[key], priceDict19, priceDict20, priceDict21, priceDict22)
#   priceDict19.update(a)
#   priceDict20.update(b)
#   priceDict21.update(c)
#   priceDict22.update(d) 
# priceDict19, priceDict20, priceDict21, priceDict22 =


###CONVIERTO DICTs Y EL RANDOM VECTOR A CSVs PARA GUARDARLOS Y USARLOS SIEMPRE :) 

# priceDict19, priceDict20, priceDict21, priceDict22 = returnPrice(path = dataset_path,priceDict19=priceDict19, priceDict20=priceDict20, priceDict21=priceDict21, priceDict22= priceDict22 )
# print("dict 2019:")
# print(priceDict19)
# print("dict 2020:")
# print(priceDict20)
# print("dict 2021:")
# print(priceDict21)
# print("dict 2022:")
# print(priceDict22)
# priceDict19["VZ"] = 61.37
# priceDict20["VZ"] = 58.71
# priceDict21["VZ"] = 51.96
# priceDict22["VZ"] = 45.34

# priceDict19["WBA"] = 58.96
# priceDict20["WBA"] = 39.85
# priceDict21["WBA"] = 52.16
# priceDict22["WBA"] = 40.87

# field_names = []
# for key in priceDict19:
#   field_names.append(key)
# dict_list = [priceDict19, priceDict20, priceDict21, priceDict22]
# with open('prices.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(dict_list)

# nStocks19, nStocks20,nStocks21,nStocks22 = priceDict19, priceDict20, priceDict21, priceDict22
# i = 0
# for key in nStocks19:
  
#   nStocks19[key] = price_vector[i]/priceDict19[key]
#   nStocks20[key] = price_vector[i]/priceDict20[key]
#   nStocks21[key] = price_vector[i]/priceDict21[key]
#   nStocks22[key] = price_vector[i]/priceDict22[key]
#   i = i+1

# print("Number of stocks in 2019:\n",nStocks19)
# print("\nNumber of stocks in 2020:\n",nStocks20)
# print("\nNumber of stocks in 2021:\n",nStocks21)
# print("\nNumber of stocks in 2022:\n",nStocks22)


