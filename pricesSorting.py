#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 10:37:21 2023

@author: madidina
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# bid price
df_bid = pd.read_csv('/Users/madidina/Library/Mobile Documents/com~apple~CloudDocs/TELECOM/3A/IIT/MATH-594/bid_Price_File_3251758.csv')
df_bid = df_bid.drop(df_bid.index[1000:])

price_bid = df_bid.iloc[:, 1] 
time_bid = df_bid.iloc[:, 0]

# offer price
df_ask = pd.read_csv('/Users/madidina/Library/Mobile Documents/com~apple~CloudDocs/TELECOM/3A/IIT/MATH-594/offer_Price_File_3251758.csv')
df_ask = df_ask.drop(df_ask.index[1000:])

price_ask = df_ask.iloc[:, 1]
time_ask = df_ask.iloc[:, 0]


#Convertion from series to array
price_bid_array = price_bid.to_numpy()
price_ask_array = price_ask.to_numpy()
time_ask_array = time_ask.to_numpy()
time_bid_array = time_bid.to_numpy()


#Time merging and sorting
time_array = time_ask_array

for i in range(len (time_bid_array) -1):
    for j in range (len(time_ask_array) - 1):
        if time_bid_array[i]>time_ask_array[j] and time_bid_array[i] < time_ask_array[j+1]:
                time_ask_array.insert(j+1, time_bid_array[i])

#Complete List of Offers
offer_array=[]
while i < (len (time_array) -1):
    for j in range(len (time_bid)-1):
        if time_array[i]==time_bid[j] or time_array[i]>time_bid[j]:
            offer_array.append(price_bid[i])
            j+=1
        else:
            offer_array.append(price_bid[i+1])
            i+=1

plt.plot(time_array,offer_array) 
plt.title('graph of the full offer')
plt.show()
