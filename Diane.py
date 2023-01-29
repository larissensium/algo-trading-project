#!/usr/bin/env python
# coding: utf-8

# In[78]:


"""
Created on Fri Jan 27 10:37:21 2023

@author: madidina
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# bid price
df_bid = pd.read_csv('./bid_Price_File_3251758.csv', header=None)
df_bid = df_bid.drop(df_bid.index[1000:])


# In[79]:


price_bid = df_bid.iloc[:, 1] 
time_bid = df_bid.iloc[:, 0]
price_bid


# In[80]:


time_bid


# In[81]:


# offer price
df_ask = pd.read_csv('./offer_Price_File_3251758.csv', header=None)
df_ask = df_ask.drop(df_ask.index[1000:])

price_ask = df_ask.iloc[:, 1]
time_ask = df_ask.iloc[:, 0]


# In[82]:


time_ask


# In[83]:


#Convertion from series to array
price_bid_array = price_bid.to_numpy()
price_ask_array = price_ask.to_numpy()
time_ask_array = time_ask.to_numpy()
time_bid_array = time_bid.to_numpy()


# In[84]:


#Time merging and sorting
def time_merging_sorting(time_ask_array,time_bid_array):
    time_array = time_ask_array

    for i in range(len (time_bid_array) -1):
        for j in range (len(time_ask_array) - 1):
            if time_bid_array[i] > time_ask_array[j] and time_bid_array[i] < time_ask_array[j+1]:
                    np.insert(time_array, j+1, time_bid_array[i])
    return time_array


# In[107]:


#Complete List of Offers
def list_completer(time_array,time_bid,price_bid):
    offer_array=[]
    i=0
    while i < (len (time_array)-1):
        for j in range(len (time_bid)-1):
            if time_array[i] == time_bid[j] or time_array[i] > time_bid[j]:
                offer_array.append(price_bid[i])
                #print("j",j)
            else:
                if(i>=999):break
                #print("i",i)
                offer_array.append(price_bid[i+1])
                i+=1
        if(j==998):i+=1
    return offer_array


# In[108]:


#Time array
time_array = time_merging_sorting(time_ask_array,time_bid_array)


# In[109]:


#For offers
offers_array = list_completer(time_array,time_bid,price_bid)


# In[110]:


#For asks
ask_arrays = list_completer(time_array,time_ask,price_ask)


# In[114]:


plt.plot(time_array[0:999],offers_array[0:999], label='offers through time')
plt.plot(time_array[0:999],ask_arrays[0:999],'r', label='asks through time')
plt.title('graph of offers and asks')
plt.legend()
plt.show()


# In[134 ]:

# Gap between offer and price 

gap_array = [ask - offer for (ask, offer) in zip (ask_arrays[0:999],offers_array[0:999])]

#Graph 
plt.plot(time_array[0:999],gap_array, label='difference through time')
plt.title('Graph of the difference between offers and asks')
plt.legend()
plt.show()

#Histogram
plt.hist(gap_array)
plt.title('histogram of the spread')
plt.show()
