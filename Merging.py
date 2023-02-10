#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:13:10 2023

@author: madidina
"""

import pandas as pd
from operator import itemgetter
import csv
#import matplotlib.pyplot as plt

# In[78]:

    
# bid file
df_bid = pd.read_csv('./bid_Price_File_3251758.csv', header=None)
df_bid = df_bid.drop(df_bid.index[1000:])

# Bid file separate into series of price and time
price_bid = df_bid.iloc[:, 1] 
time_bid = df_bid.iloc[:, 0]
#price_bid


# In[80]:


#time_bid


# In[81]:


# Offer file
df_ask = pd.read_csv('./offer_Price_File_3251758.csv', header=None)
df_ask = df_ask.drop(df_ask.index[1000:])

# Offer file separate into series of price and time
price_ask = df_ask.iloc[:, 1]
time_ask = df_ask.iloc[:, 0]


# In[82]:


#time_ask


# In[83]:


#Convertion from series to array
price_bid_array = price_bid.to_numpy()
price_ask_array = price_ask.to_numpy()
time_ask_array = time_ask.to_numpy()
time_bid_array = time_bid.to_numpy()

# In[111]:

def merging (time_ask_array,time_bid_array):
    
    a = len(time_ask_array)
    b = len(time_bid_array)
    
    #ask = np.empty(shape=(a,3))
    ask = []
    #bid = np.empty(shape=(b,3))
    bid = []
    
    for i in range(0,a):
        #ask[i] = [time_ask_array[i],'a',i]
        ask.append([time_ask_array[i],'a',i])

    
    for j in range(0,b):
        #bid[j] = [time_bid_array[j],'b',b]
        bid.append([time_bid_array[j],'b',j])
    
    merging_array = bid + ask
    res = sorted(merging_array, key = itemgetter(0))

    return res
  
# In[111]:
    
Final = merging (time_ask_array,time_bid_array)

# In[112]:
# CSV file importation 

# field name 
fields = ['Time', 'Ask_Bid', 'Row']

with open('MergedTime', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(Final)