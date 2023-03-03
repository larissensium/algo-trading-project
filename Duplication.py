#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:12:53 2023

@author: madidina
"""

import pandas as pd
import csv

merge_file = open('./MergedTimeBis')
bid_file = open('./bid_Price_File_3251758.csv')
offer_file = open('./offer_Price_File_3251758.csv')

# In[1]:
# Function that creat a file with times and prices for the input csv
 
def dupication(total_file, b_file, o_file):
    
    """
    INPUTS
    total_file is the csv file were we find the time, offer or bid indication, index of the price in the original csv file
    b_file is the original csv file of bid
    o_file is the original csv file of offer

    OUTPUTS 
    None
    
    WHAT DOES IT DO ?
    Creation of csv files one for the bid and one offer with ['Time', 'Price'] as field
    """
    
    # Read csv: sep default ‘,’
    csv_merge_file = pd.read_csv(merge_file)
    csv_offer_file = pd.read_csv(offer_file)
    csv_bid_file = pd.read_csv(bid_file)
    
    # Init Lists
    bid_list = [[0,0]]
    offer_list = [[0,0]]
    
    print('lists creation')

    for index,row in csv_merge_file.iterrows():
        
        selected_row = row[2]
        
        if (selected_row == len(csv_bid_file)) or (selected_row == len(csv_offer_file)):
            selected_row-=1
     
        # Acces specific row and coloumn in a csv file
        
        if (row[1]=='b'):
            bid_list.append([csv_bid_file.loc[selected_row,:][0],csv_bid_file.loc[selected_row,:][1]])
            offer_list.append(offer_list[-1])
            
        elif (row[1]=='bo'):
            bid_list.append([csv_bid_file.loc[selected_row,:][0],csv_bid_file.loc[selected_row,:][1]])
            offer_list.append([csv_offer_file.loc[row[3],:][0],csv_offer_file.loc[row[3],:][1]])
        
        else:
            bid_list.append(bid_list[-1])
            offer_list.append([csv_offer_file.loc[selected_row,:][0],csv_offer_file.loc[selected_row,:][1]])

    # CSV file creation
    print('csv creation')
    
    # field name 
    fields = ['Time', 'Price']
    
    with open('Bid', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerow(fields)
        write.writerows(bid_list)
        
    with open('Offer', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerow(fields)
        write.writerows(offer_list)
        
# In[]:

def combinaison(total_file, b_file, o_file):
    
    """
    INPUTS
    total_file is the csv file were we find the time, offer or bid indication, index of the price in the original csv file
    b_file is the original csv file of bid
    o_file is the original csv file of offer

    OUTPUTS 
    None
    
    WHAT DOES IT DO ?
    Creation of one csv fileof['Bid_Time', 'Bid_Price', 'Offer_Time', 'Offer_Price', 'Spread_Time', 'Spread']
    """
    
    # Read csv: sep default ‘,’
    csv_merge_file = pd.read_csv(merge_file)
    csv_offer_file = pd.read_csv(offer_file)
    csv_bid_file = pd.read_csv(bid_file)
    
    # Init Lists
    total_list=[[0,0,0,0,0,0]]
    
    print('lists creation')

    for index,row in csv_merge_file.iterrows():
        
        selected_row = row[2]
        
        if (selected_row == len(csv_bid_file)) or (selected_row == len(csv_offer_file)):
            selected_row-=1
     
        # Acces specific row and coloumn in a csv file
        
        if (row[1]=='b'):
            total_list.append([ csv_bid_file.loc[selected_row,:][0],csv_bid_file.loc[selected_row,:][1],
                                total_list[-1][2],total_list[-1][3],
                                csv_merge_file.loc[selected_row,:][0],
                                total_list[-1][3] - csv_bid_file.loc[selected_row,:][1] ])
            
        elif (row[1]=='bo'):
            total_list.append([ csv_bid_file.loc[selected_row,:][0],csv_bid_file.loc[selected_row,:][1],
                                csv_offer_file.loc[row[3],:][0],csv_offer_file.loc[row[3],:][1],
                                csv_merge_file.loc[selected_row,:][0],
                                csv_offer_file.loc[row[3],:][1] - csv_bid_file.loc[selected_row,:][1]])
            
        else:
            total_list.append([ total_list[-1][0],total_list[-1][1],
                                csv_offer_file.loc[selected_row,:][0],csv_offer_file.loc[selected_row,:][1],
                                csv_merge_file.loc[selected_row,:][0],
                                csv_offer_file.loc[selected_row,:][1] - total_list[-1][1]])
            
    # CSV file creation
    print('csv creation')
    
    # field name 
    fields = ['Bid_Time', 'Bid_Price', 'Offer_Time', 'Offer_Price', 'Spread_Time', 'Spread']
    
    with open('Total_File', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerow(fields)
        write.writerows(total_list)      
        
  # In[]:

dupication(merge_file, bid_file, offer_file)    

combinaison(merge_file, bid_file, offer_file)


   