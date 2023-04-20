import pandas as pd
import numpy as np
import os   
my_path= '/home/victor/Documentos/GitHub/nasdaq/nasdaq_nosp500_15minutos'

RES_1 =0
RES_2 = 10
RES_3 = 15

def samples(df, smp):
  smp_list =[]
  missing_list = []
  for i in range(570,960):
    smp_list.append(i)
    #print(i)
  r, c = df.shape
  #print(df['time'].values)
  #print("Aquí viene el for...\n\n\n")
  for j in range(0,len(smp_list)):
    if smp_list[j] not in df['time'].values:
      missing_list.append(smp_list[j])
  #print(missing_list)
  print(missing_list)
# asdf = samples2(df, 15)
  aux = df
  first = True
  for k in range(0,len(missing_list)):
    if first == True:
      if missing_list[k]< df.shape[0]:
        aux = df.iloc[:(missing_list[k]-570)]
        data = {'time': missing_list[k], 'open': [df['open'].values[missing_list[k]-570]],'high': [df['high'].values[missing_list[k]-570]], 'low': [df['low'].values[missing_list[k]-570]], 'close': [df['close'].values[missing_list[k]-570]], 'volume': [df['volume'].values[missing_list[k]-570]]}
        append_this = pd.DataFrame(data = data)
        #print(df['time'].values[missing_list[k]-570-1])
        aux = pd.concat([aux, append_this], ignore_index=True)
        aux = pd.concat([aux, df.iloc[missing_list[k]-570:]], ignore_index=True)
        first = False
      else:
        aux = aux.iloc[:(missing_list[k]-570)]
        data = {'time': missing_list[k], 'open': [df['open'].values[-1]],'high': [df['high'].values[-1]], 'low': [df['low'].values[-1]], 'close': df['close'].values[-1], 'volume': [df['volume'].values[-1]]}
        append_this = pd.DataFrame(data = data)
        aux = pd.concat([aux, append_this], ignore_index=True)
        aux = pd.concat([aux, df.iloc[missing_list[k]-570-k:]], ignore_index=True)
    else: 
      #print("empieza else")
      if missing_list[k] < df.shape[0]:
        aux = aux.iloc[:(missing_list[k]-570)]
        data = {'time': missing_list[k], 'open': [df['open'].values[missing_list[k]-570-1]],'high': [df['high'].values[missing_list[k]-570-1]], 'low': [df['low'].values[missing_list[k]-570-1]], 'close': [df['close'].values[missing_list[k]-570-1]], 'volume': [df['volume'].values[missing_list[k]-570-1]]}
        append_this = pd.DataFrame(data = data)
        aux = pd.concat([aux, append_this], ignore_index=True)
        aux = pd.concat([aux, df.iloc[missing_list[k]-570-k:]], ignore_index=True)
      else:
        aux = aux.iloc[:(missing_list[k]-570)]
        data = {'time': missing_list[k], 'open': [df['open'].values[-1]],'high': [df['high'].values[-1]], 'low': [df['low'].values[-1]], 'close': df['close'].values[-1], 'volume': [df['volume'].values[-1]]}
        append_this = pd.DataFrame(data = data)
        aux = pd.concat([aux, append_this], ignore_index=True)
        aux = pd.concat([aux, df.iloc[missing_list[k]-570-k:]], ignore_index=True)

      #print("acaba else")
  #print("For de missing terminado")
  #aux = pd.concat([aux, df.iloc[(aux['time'].values[-1]-570):]])
  #print(aux.iloc[(700-570):(750-570)])

  
  aux = aux[['time', 'close', 'volume']]
  #print(aux.iloc[(700-570):(750-570)])
  #print(aux.iloc[(800-570):(850-570)])
  for i  in range(1,len(aux)):
        if i % (smp) != 0:
          aux = aux.drop(i-1)
  return aux


def find_files(path):
  files = os.listdir(path)
  cancelled_days = []
  for item in files:    
    if os.path.isdir(os.path.join(path, item)):
      find_files(os.path.join(path, item))
    else:
      file_csv = os.path.join(path, item)
      print('Opened' + file_csv)
      if file_csv[-12:-4] in cancelled_days:
        pass
      else:
        df = pd.read_csv(file_csv)
        totalNan = 390-len(df['time'])
        if totalNan>5000:
          #Ver qué pasa con DJ 
          print("Not enough samples for day: ", file_csv[-12:-4])
          cancelled_days.append(file_csv[-12:-4])
        else:
          df = samples(df,smp = RES_3)
          [n,v_path] = str(file_csv).split(path)
          save_path = save_csv_path + v_path
          df.to_csv(save_path)

my_path = '/home/victor/Documentos/GitHub/nasdaq/nasdaq_nosp500_15minutos'
save_csv_path ='/home/victor/Documentos/Github/nasdaq/csv_buenos'
find_files(my_path)
