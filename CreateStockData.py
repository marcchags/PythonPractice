# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:01:42 2017

@author: marcc
"""

import pandas as pd
import numpy as np
import sys
#import matplotlib.pyplot as plt

fname = input('Please enter csv filename: ')

df = pd.read_csv(fname, header=0, parse_dates=True, index_col='Date')   
df = df.drop(['Open','High','Low','Close'], axis='columns')
df['Return'] = np.nan
df['Year'] = df.index.year
df['sma20'] = df['Adj Close'].rolling(window=20).mean()
df['std'] = df['Adj Close'].rolling(window=20).std()
print(df.columns)

for a in range(1,(len(df)-1)):
    #calculates daily return %
    b = a - 1
    df.iloc[a, 2] = ((df.iloc[a,0])/(df.iloc[b,0])) - 1

print(df['Return'][df['Return']==0].count())
print('Median: ' + str(df['Return'].median()))
print('Mean: ' + str(df['Return'].mean()))
#df['Return'].plot(kind='hist', bins = 100)
y = 10000 / df.iloc[0,0]

z = y * df.iloc[-1,0]
print(z)


#plt.show()
