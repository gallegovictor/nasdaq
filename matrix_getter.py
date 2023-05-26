import os
import pandas as pd
import numpy as np 
from MyUtils import * 

import random


folder_path = '/home/victor/Escritorio/nasdaq_ind_returns/'  # Replace with the actual folder path where the CSV files are located


text = """
AAPL.US.csv  AVGO.US.csv   DXCM.US.csv   INTC.US.csv  MSFT.US.csv  ROST.US.csv
ABNB.US.csv  AZN.US.csv    EA.US.csv     INTU.US.csv  MU.US.csv    SBUX.US.csv
ADBE.US.csv  BIIB.US.csv   EBAY.US.csv   ISRG.US.csv  NFLX.US.csv  SGEN.US.csv
ADI.US.csv   CDNS.US.csv   ENPH.US.csv   JD.US.csv    NVDA.US.csv  SIRI.US.csv
ADP.US.csv   CHTR.US.csv   FANG.US.csv   KLAC.US.csv  NXPI.US.csv  SNPS.US.csv
ADSK.US.csv  CMCSA.US.csv  FAST.US.csv   LCID.US.csv  ODFL.US.csv  TEAM.US.csv
AEP.US.csv   COST.US.csv   FISV.US.csv   LRCX.US.csv  ORLY.US.csv  TMUS.US.csv
ALGN.US.csv  CPRT.US.csv   FTNT.US.csv   LULU.US.csv  PANW.US.csv  TSLA.US.csv
AMAT.US.csv  CRWD.US.csv   GFS.US.csv    MAR.US.csv   PAYX.US.csv  TXN.US.csv
AMD.US.csv   CSCO.US.csv   GILD.US.csv   MDLZ.US.csv  PCAR.US.csv  VRSK.US.csv
AMGN.US.csv  CSX.US.csv    GOOGL.US.csv  MELI.US.csv  PDD.US.csv   VRTX.US.csv
AMZN.US.csv  CTAS.US.csv   GOOG.US.csv   META.US.csv  PEP.US.csv   WDAY.US.csv
ANSS.US.csv  CTSH.US.csv   HON.US.csv    MNST.US.csv  QCOM.US.csv  XEL.US.csv
ASML.US.csv  DDOG.US.csv   IDXX.US.csv   MRNA.US.csv  REGN.US.csv  ZM.US.csv
ATVI.US.csv  DLTR.US.csv   ILMN.US.csv   MRVL.US.csv  RIVN.US.csv  ZS.US.csv
"""
tickers_list = sorted(text.split())
df_result = pd.DataFrame()
# Get a list of file paths using os module
for t in tickers_list:
    path = folder_path + t
    df = pd.read_csv(path)
    r,c = df.shape
    if r != 18750:
       df = MyUtils.add_random_rows(df, (18750-r))
    col_name = t.replace(".csv", "")
    df_result[col_name] = df[df.columns[1]].values
    print(path + " transformed succesfully-")
# Create an empty list to store the DataFrames
df_result.to_csv('/home/victor/Escritorio/matrix.csv')

# Loop through the file paths and read each CSV file into a DataFrame
# for file in csv_files:
#     df = pd.read_csv(file)
#     print("Columns: ", df.columns)
#     dfs.append(df[df.columns[1]].values)
#     print(dfs)

# # Concatenate all the DataFrames into a single DataFrame
# combined_df = pd.concat(dfs, ignore_index=True)
