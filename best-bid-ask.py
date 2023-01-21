#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:13:29 2022

@author: laramatiukha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# bid price

df_bid = pd.read_csv('/Users/laramatiukha/Desktop/bid_Price_File_3251758-2.csv')

price_bid = df_bid.iloc[:, 1] 
time_bid = df_bid.iloc[:, 0]

# checking if there are any empty entries 
# empty_p_bid = price_bid.eq('').sum()
# empty_t_bid = time_bid.eq('').sum()

plt.plot(time_bid,price_bid)
plt.xlabel('time')
plt.ylabel('best bid price')
plt.show()


# offer price
df_ask = pd.read_csv('/Users/laramatiukha/Desktop/offer_Price_File_3251758.csv')

# since len(df_ask) > len(df_bid)
df_ask = df_ask.drop(df_ask.index[381323:388638])

price_ask = df_ask.iloc[:, 1]
time_ask = df_ask.iloc[:, 0]

plt.plot(time_ask,price_ask,color='g')
plt.xlabel('time')
plt.ylabel('best ask price')
plt.show()

price_bid_array = price_bid.to_numpy()
price_ask_array = price_ask.to_numpy()


# spred = price ask - price bid 
spread = price_ask_array - price_bid_array

# histogram
plt.hist(spread)
plt.title('histogram of the spread')
plt.show()


# graph 
plt.plot(spread,color='k')
plt.title('graph of the spread')
plt.show()
