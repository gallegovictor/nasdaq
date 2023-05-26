import os
import pandas as pd
import numpy as np 
from MyUtils import * 

import random

def assign_random_values(n, values_list):
    if n <= 0:
        return values_list  # Return the original list if n is zero or negative
    
    random_values = random.sample(values_list, n)  # Select n random values
    
    values_list.extend(random_values)  # Extend the original list with the random values
    
    return values_list

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5

# modified_list = assign_random_values(n, my_list)
# print(modified_list)



text = '''
AAPL.US ANSS.US CSCO.US FAST.US ISRG.US MRVL.US PEP.US TXN.US
ABNB.US ASML.US FISV.US JD.US MSFT.US QCOM.US VRSK.US
ADBE.US ATVI.US CSX.US FTNT.US KLAC.US MU.US REGN.US VRTX.US
ADI.US AVGO.US CTAS.US GFS.US LCID.US NFLX.US RIVN.US WDAY.US
ADP.US AZN.US CTSH.US GILD.US LRCX.US NVDA.US ROST.US XEL.US
ADSK.US BIIB.US DDOG.US GOOGL.US LULU.US NXPI.US SBUX.US ZM.US
AEP.US CDNS.US DLTR.US GOOG.US MAR.US ODFL.US SGEN.US ZS.US
ALGN.US CHTR.US DXCM.US HON.US MDLZ.US ORLY.US SIRI.US
AMAT.US CMCSA.US EA.US IDXX.US MELI.US PANW.US SNPS.US
AMD.US COST.US EBAY.US ILMN.US META.US PAYX.US TEAM.US
AMGN.US CPRT.US ENPH.US INTC.US MNST.US PCAR.US TMUS.US
AMZN.US CRWD.US FANG.US INTU.US MRNA.US PDD.US TSLA.US
'''

# Split the text into a list and sort it alphabetically
stocks_list = sorted(text.split())

years = ['2021','2022', '2023']
#folder_path = '/home/victor/Escritorio/nasdaq_returns/AAPL/'  # Replace with the path to your folder

# Initialize an empty list to store the second column values
df_result = pd.DataFrame()
for s in stocks_list:

    second_column_values = []

    for y in years:
        
        folder_path = '/home/victor/Escritorio/nasdaq_returns/' + s+ '/' + y  + '/'  # Replace with the path to your folder
        # Iterate over the files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):  # Check if the file is a CSV file
                file_path = os.path.join(folder_path, filename)
                
                # Read the CSV file
                df = pd.read_csv(file_path)
                
                # Extract the second column values
                column_values = df.iloc[:, 2].tolist()  # Assuming the second column index is 1
                
                # Append the column values to the list
                second_column_values.extend(column_values)
                print(file_path + " transformed successfully.")
        # Create a DataFrame column using the extracted values
        #df_column = pd.DataFrame({'SecondColumn': second_column_values})
    # if len(second_column_values) != 18750:
    #     second_column_values = assign_random_values((18750-len(second_column_values)), second_column_values)
    # df_result[s] = second_column_values
    df_result = pd.DataFrame({s: second_column_values})
    save_here = '/home/victor/Escritorio/nasdaq_ind_returns/' + s + '.csv'
    df_result.to_csv(save_here)
        # Print the DataFrame column
print("Transformation ended successfully.")
#df_result.to_csv('/home/victor/Escritorio/nasdaq_test.csv')
