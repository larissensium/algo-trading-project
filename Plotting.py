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
time_array = csv_merge_file.iloc[:, 0].tolist()
bid_array = ['Nan']
offer_array = ['Nan']

# Import data 

for index,row in csv_merge_file.iterrows():
    #time_array.append(row)
    if (row[1]=='b'):
        # Acces specific row and coloumn in a csv file
        bid_array.append(csv_bid_file.loc[row[2],:][1])
        offer_array.append(offer_array[-1])
        
    else:
        bid_array.append(bid_array[-1])
        offer_array.append(csv_offer_file.loc[row[2],:][1])
        
plt.plot(time_array,offer_array, title='Offer')
plt.plot(time_array,bid_array, title='Bid')
plt.legend()
plt.show()
