#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Mon Feb 13 09:04:10 2023

#@author: madidina

import pandas as pd
import matplotlib.pyplot as plt

# Open
merge_file = open('./MergedTimeBis')
bid_file = open('./bid_Price_File_3251758.csv')
offer_file = open('./offer_Price_File_3251758.csv')

# Read csv: sep default ‘,’
csv_merge_file = pd.read_csv(merge_file)
csv_offer_file = pd.read_csv(offer_file)
csv_bid_file = pd.read_csv(bid_file)

# Init Lists
time_list = csv_merge_file.iloc[:, 0].tolist()
bid_list = [0]
offer_list = [0]
spread_list = []

print('lists creation')
# Import data 
for index,row in csv_merge_file.iterrows():
    
    selected_row = row[2]
    
    if (selected_row == len(csv_bid_file)) or (selected_row == len(csv_offer_file)):
        selected_row-=1
 
    # Acces specific row and coloumn in a csv file
    
    if (row[1]=='b'):
        bid_list.append(csv_bid_file.loc[selected_row,:][1])
        offer_list.append(offer_list[-1])
        spread_list.append(offer_list[-1] - bid_list[-1])
        
    elif (row[1]=='bo'):
        bid_list.append(csv_bid_file.loc[selected_row,:][1])
        offer_list.append(csv_offer_file.loc[row[3],:][1])
        spread_list.append(offer_list[-1] - bid_list[-1])
    
    else:
        bid_list.append(bid_list[-1])
        offer_list.append(csv_offer_file.loc[selected_row,:][1])
        spread_list.append(offer_list[-1] - bid_list[-1])

    if (spread_list[-1]<0):
        print(f' row: {row}\n index: {index}\n time: {time_list[index]}\n Bid: {bid_list[-1]}\n Offer: {offer_list[-1]}\n\n')

print ('lists created')

plt.plot(time_list[1:],offer_list[1:-1], label='Offer')
plt.plot(time_list[1:],bid_list[1:-1], label='Bid')
plt.legend()
plt.show()

plt.plot(time_list[1:],spread_list[1:], label='Spread')
plt.legend()
plt.show()

## histogram of the spread
plt.hist(spread_list[1:],bins=np.linspace(-1, 10, num=100))
plt.show()


from collections import Counter
Counter(spread_list) # counts of all values of the spread 

# most common values of the spread:
# 1.0: 438983 - # of occurances of 1 in spread list 
# 2.0: 14990,
# 0.5: 112188
# 1.5: 139287


spread_1 = spread_list.count(1)
percent_1 = spread_1/len(spread_list) # 0.5709055771441651
print('counts of spread = 1:', spread_1 ,'\npercentage of all spread values: ',percent_1,'\n')

spread_2 = spread_list.count(2)
percent_2 = spread_2/len(spread_list)
print('counts of spread = 2:', spread_2 ,'\npercentage of all spread values: ',percent_2,'\n')

# idk maybe 0.5 and 1.5 not needed 
spread_05 = spread_list.count(0.5)
percent_05 = spread_05/len(spread_list) # 0.14590258595127736
print('counts of spread = 0.5:', spread_05 ,'\npercentage of all spread values: ',percent_05,'\n')

spread_1_5 = spread_list.count(1.5)
percent_1_5 = spread_1_5/len(spread_list) # 0.18114534076189584
print('counts of spread = 1.5:', spread_1_5 ,'\npercentage of all spread values: ',percent_1_5,'\n')
# Info : 4 minutes of running time
