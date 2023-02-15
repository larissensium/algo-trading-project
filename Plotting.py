#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Mon Feb 13 09:04:10 2023

#@author: madidina

import pandas as pd
import matplotlib.pyplot as plt

# Open
merge_file = open('./MergedTime')
bid_file = open('./bid_Price_File_3251758.csv')
offer_file = open('./offer_Price_File_3251758.csv')

# Read csv: sep default ‘,’
csv_merge_file = pd.read_csv(merge_file)
csv_offer_file = pd.read_csv(offer_file)
csv_bid_file = pd.read_csv(bid_file)

# Init Arrays
time_list = csv_merge_file.iloc[:, 0].tolist()
bid_list = ['Nan']
offer_list = ['Nan']
spread_list = []

# Import data 

for index,row in csv_merge_file.iterrows():
    #time_list.append(row)
    if (row[1]=='b'):
        # Acces specific row and coloumn in a csv file
        bid_list.append(csv_bid_file.loc[row[2],:][1])
        offer_list.append(offer_list[-1])
        spread_list.append(bid_list[-1] - offer_list[-1])
        
    else:
        bid_list.append(bid_list[-1])
        offer_list.append(csv_offer_file.loc[row[2],:][1])
        spread_list.append(bid_list[-1] - offer_list[-1])

#spread = [(o - b) for o, b in zip(offer_list, bid_list)]
#spread = np.array(offer_list)-np.array(bid_list)

plt.plot(time_list[:-3],offer_list, label='Offer')
plt.plot(time_list[:-3],bid_list, label='Bid')
plt.legend()
plt.show()

plt.plot(time_list[:-3],spread_list, label='Spread')
plt.legend()
plt.show()
