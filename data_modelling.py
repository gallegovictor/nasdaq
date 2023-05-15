# import pandas as pd
# import numpy as np
# import os   
# my_path= '/home/victor/Documentos/GitHub/nasdaq/nasdaq_nosp500_15minutos'

# RES_1 =0
# RES_2 = 10
# RES_3 = 15

# # def samples(df, smp):
# #   smp_list =[]
# #   missing_list = []
# #   for i in range(570,960):
# #     smp_list.append(i)
# #     #print(i)
# #   r, c = df.shape
# #   #print(df['time'].values)
# #   #print("Aquí viene el for...\n\n\n")
# #   for j in range(0,len(smp_list)):
# #     if smp_list[j] not in df['time'].values:
# #       missing_list.append(smp_list[j])
# #   #print(missing_list)
# #   print(missing_list)
# # # asdf = samples2(df, 15)
# #   aux = df
# #   first = True
# #   for k in range(0,len(missing_list)):
# #     if first == True:
# #       if missing_list[k]< df.shape[0]:
# #         aux = df.iloc[:(missing_list[k]-570)]
# #         data = {'time': missing_list[k], 'open': [df['open'].values[missing_list[k]-570]],'high': [df['high'].values[missing_list[k]-570]], 'low': [df['low'].values[missing_list[k]-570]], 'close': [df['close'].values[missing_list[k]-570]], 'volume': [df['volume'].values[missing_list[k]-570]]}
# #         append_this = pd.DataFrame(data = data)
# #         #print(df['time'].values[missing_list[k]-570-1])
# #         aux = pd.concat([aux, append_this], ignore_index=True)
# #         aux = pd.concat([aux, df.iloc[missing_list[k]-570:]], ignore_index=True)
# #         first = False
# #       else:
# #         aux = aux.iloc[:(missing_list[k]-570)]
# #         data = {'time': missing_list[k], 'open': [df['open'].values[-1]],'high': [df['high'].values[-1]], 'low': [df['low'].values[-1]], 'close': df['close'].values[-1], 'volume': [df['volume'].values[-1]]}
# #         append_this = pd.DataFrame(data = data)
# #         aux = pd.concat([aux, append_this], ignore_index=True)
# #         aux = pd.concat([aux, df.iloc[missing_list[k]-570-k:]], ignore_index=True)
# #     else: 
# #       #print("empieza else")
# #       if missing_list[k] < df.shape[0]:
# #         aux = aux.iloc[:(missing_list[k]-570)]
# #         data = {'time': missing_list[k], 'open': [df['open'].values[missing_list[k]-570-1]],'high': [df['high'].values[missing_list[k]-570-1]], 'low': [df['low'].values[missing_list[k]-570-1]], 'close': [df['close'].values[missing_list[k]-570-1]], 'volume': [df['volume'].values[missing_list[k]-570-1]]}
# #         append_this = pd.DataFrame(data = data)
# #         aux = pd.concat([aux, append_this], ignore_index=True)
# #         aux = pd.concat([aux, df.iloc[missing_list[k]-570-k:]], ignore_index=True)
# #       else:
# #         aux = aux.iloc[:(missing_list[k]-570)]
# #         data = {'time': missing_list[k], 'open': [df['open'].values[-1]],'high': [df['high'].values[-1]], 'low': [df['low'].values[-1]], 'close': df['close'].values[-1], 'volume': [df['volume'].values[-1]]}
# #         append_this = pd.DataFrame(data = data)
# #         aux = pd.concat([aux, append_this], ignore_index=True)
# #         aux = pd.concat([aux, df.iloc[missing_list[k]-570-k:]], ignore_index=True)

# #       #print("acaba else")
# #   #print("For de missing terminado")
# #   #aux = pd.concat([aux, df.iloc[(aux['time'].values[-1]-570):]])
# #   #print(aux.iloc[(700-570):(750-570)])

  
# #   aux = aux[['time', 'close', 'volume']]
# #   #print(aux.iloc[(700-570):(750-570)])
# #   #print(aux.iloc[(800-570):(850-570)])
# #   for i  in range(1,len(aux)):
# #         if i % (smp) != 0:
# #           aux = aux.drop(i-1)
# #   return aux


# # def find_files(path):
# #   files = os.listdir(path)
# #   cancelled_days = []
# #   for item in files:    
# #     if os.path.isdir(os.path.join(path, item)):
# #       find_files(os.path.join(path, item))
# #     else:
# #       file_csv = os.path.join(path, item)
# #       print('Opened' + file_csv)
# #       if file_csv[-12:-4] in cancelled_days:
# #         pass
# #       else:
# #         df = pd.read_csv(file_csv)
# #         totalNan = 390-len(df['time'])
# #         if totalNan>5000:
# #           #Ver qué pasa con DJ 
# #           print("Not enough samples for day: ", file_csv[-12:-4])
# #           cancelled_days.append(file_csv[-12:-4])
# #         else:
# #           df = samples(df,smp = RES_3)
# #           [n,v_path] = str(file_csv).split(path)
# #           save_path = save_csv_path + v_path
# #           df.to_csv(save_path)

# my_path = '/home/victor/Documentos/GitHub/nasdaq/nasdaq_nosp500_15minutos'
# save_csv_path ='/home/victor/Documentos/Github/nasdaq/csv_buenos'
# #find_files(my_path)

# def read_csv_files(path):
#     all_data = []
#     first_iter = True 
#     append_it = pd.DataFrame()
#     result = pd.DataFrame()
#     for foldername, subfolders, filenames in os.walk(path):
#         for filename in filenames:
#             if filename.endswith('.csv'):
#                 csv_path = os.path.join(foldername, filename)
#                 instrument = csv_path.split('/')[7]
#                 print(instrument)
#                 df = pd.read_csv(csv_path)
#                 df = df.drop(columns=[df.columns[1], df.columns[2], df.columns[3]])
#                 if first_iter == True:
#                   first_iter = False
#                   append_it['time'] = df['time']
#                   #append_it[instrument] = df['close'].values
#                   result = pd.concat([result ,append_it['time']], axis=1)
#                   #aux_instrument = instrument 
#                   #all_data.append(append_it)
#                   aux_instrument = None
#                 if instrument == aux_instrument:
#                   result.loc[:, instrument] = result[instrument].append(pd.Series(df['close'].values))
#                 else: 
#                   aux_instrument = instrument
#                   append_it[instrument] = df['close'].values
#                   result = pd.concat([result, append_it[instrument]], axis=1)

#                 print(result.head())
#                 print("\n\n\nFile " + csv_path + " was read succesfully\n\n\n")
#     return pd.concat(all_data)

# # # Example usage:
# # all_csv_data = read_csv_files('/path/to/folder')
# # print(all_csv_data.head())

# result = read_csv_files(my_path)

# print(result.head())

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
    var_dict = globList[i].split('/')[5]
    print(var_dict)
    myDict[var_dict] = globList[i]
  return dict(sorted(myDict.items()))

rand_vector = MyUtils.random_W(91)
price_vector = [0]*len(rand_vector)
for i  in range(0, len(price_vector)):
  price_vector[i] = MyUtils.PORTFOLIO_PRICE*rand_vector[i]
#   print("This is the amount of dollars for each instrument in a portfolio of 10000$:\n", price_vector)


dataset_path = '/home/victor/Escritorio/nasdaq_completed/**'
pathDict = globPaths(dataset_path)
print("\n\n", pathDict)
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
save_returns_iter = '/home/victor/Escritorio/nasdaq_returns'
for v in pathList.values():
  print('Iterating thru: '+v)
  df = pd.read_csv(v)
  df = df.drop(['open', 'high', 'low'], axis=1)
  array = np.asarray(df)
  [rows, columns] = array.shape
  returns = MyUtils.computeDailyReturns(array,rows, columns)
  returns = pd.DataFrame(returns, columns=['time', 'close', 'volume'])
  aux_volume = df.drop(['time', 'close'], axis =1)
  df = df.drop(['close', 'volume'], axis=1)
  returns = returns.drop(['time'], axis=1)
  df = df.join(returns)
  df = df.drop(['volume'],axis=1)
  df = df.join(aux_volume)
  [n,v_path] = str(v).split("/home/victor/Escritorio/nasdaq_completed")
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


