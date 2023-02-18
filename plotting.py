#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:31:30 2023

@author: laramatiukha
"""



import pandas as pd
import matplotlib.pyplot as plt
import time

t0 = time.clock()

# Open
merge_file = open('/Users/laramatiukha/Desktop/MergedTime')
bid_file = open('/Users/laramatiukha/Desktop/bid_Price_File_3251758-2.csv')
offer_file = open('/Users/laramatiukha/Desktop/offer_Price_File_3251758.csv')

# Read csv: sep default ‘,’
csv_merge_file = pd.read_csv(merge_file)
csv_offer_file = pd.read_csv(offer_file)
csv_bid_file = pd.read_csv(bid_file)

# Init Lists
time_list = csv_merge_file.iloc[:, 0].tolist()
bid_list = [0]
offer_list = [0]
spread_list = []

# Import data 
for index,row in csv_merge_file.iterrows():
    #time_list.append(row)
    if (row[1]=='b'):
        # Acces specific row and coloumn in a csv file
        bid_list.append(csv_bid_file.loc[row[2],:][1]) # initially this line gave me a Key Error "382323" (which is also length of time_list
        offer_list.append(offer_list[-1])
        spread_list.append(offer_list[-1] - bid_list[-1])
        
    else:
        bid_list.append(bid_list[-1]) 
        offer_list.append(csv_offer_file.loc[row[2],:][1])
        spread_list.append(offer_list[-1] - bid_list[-1]) # since spread = offer - bid

print ('lists creat')
#spread = [(o - b) for o, b in zip(offer_list, bid_list)]
#spread = np.array(offer_list)-np.array(bid_list)

plt.plot(time_list, offer_list[:-1], label='Offer') # since len(time_list) < len(offer_list)
plt.plot(time_list,bid_list[:-1], label='Bid') # len(time_list) < len(bid_list)
plt.legend()
plt.show()

plt.plot(time_list,spread_list, label='Spread')
plt.legend()
plt.show()

print(t0)
