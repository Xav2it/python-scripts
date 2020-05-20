#!/usr/bin/env python
# coding: utf-8

# In[2]:


import datetime
import pandas as pd
import requests
import numpy as np
from tqdm import tqdm


    
df_results = pd.read_csv('LastQuarterSpot.csv')
df_results.columns = ['id', 'currency pair', 'Datetimestamp', 'toDelete', 'price']

df_results['log_return'] = np.nan
df_results['Datetimestamp'] = pd.to_datetime(df_results['Datetimestamp'])
df_results.set_index('Datetimestamp', inplace= True)
df_results.drop(['toDelete'],axis =1, inplace=True)

currencyList = df_results['currency pair'].unique()
dfList = []
total_result = pd.DataFrame()
# Go through the different currencies to produce separate files
for i in currencyList :
    
    
    tempdf = pd.DataFrame()
    Dailyvalues = pd.DataFrame()
    

    # Here we build a list of index values corresponding to the first line of each day
    # It is used below to filter values to include in the log return

    firstDailyLinesID = df_results.groupby(df_results.index.day).first().id.to_list()

    # Now we run through the dataframe to calculate the log return
    for i in range(1,len(df_results)) :
        # log return calculation excluding the first line of each day
        if i not in firstDailyLinesID :
            df_results['log_return'][i] = np.log(df_results['price'][i]/df_results['price'][i-1])


df_results
df_results.to_excel('export_log_return.xlsx')


# In[ ]:




