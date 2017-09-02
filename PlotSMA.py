# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:45:58 2017

@author: marcc
"""
import numpy
import pandas as pd
import matplotlib.pyplot as plt

fname = 'PlotVOOSMA.csv'

df = pd.read_csv(fname, index_col=3, parse_dates=True)
x = df.index.values[-500:]
y = -500


#df = pd.DataFrame(file)


"""
y1 = file[:,0]
y2 = file[:,1]
y3 = file[:,2]
x = file[:,3]
"""


"""
df.iloc[:,0].plot(label='Closing Price VOO')
df.iloc[:,1].plot(label='SMA(50)')
df.iloc[:,2].plot(label='SMA(20)')
"""
"""
df.loc[:,['price']].plot(label='Closing Price')
df.loc[:,['sma50']].plot(lavel='SMA(50)')
df.loc[:,['sma20']].plot(label='SMA(20)')

df.loc[:,['clpls50']].plot()
df.loc[:,['clmis50']].plot()
df.loc[:,['clpls20']].plot()
df.loc[:,['clmis20']].plot()
#df[1].plot(title='SMA(50)')
#df[2].plot(title='SMA(20)')
"""

name=list(df.iloc[[0],[0]])
plt.plot(df.iloc[y:,[0]], label=name, color='blue', alpha=.50)
plt.plot(df.loc[x,['sma50pls']], label='BB50', color='#9400D3', alpha=.45)
plt.plot(df.loc[x,['sma50mis']], label='BB50', color='#9400D3', alpha=.45)
plt.plot(df.loc[x,['sma20pls']], label='BB20', color='#006400', alpha=.60)
plt.plot(df.loc[x,['sma20mis']], label='BB20', color='#006400', alpha=.60)

plt.plot(df.loc[x,['sma50']], label='SMA50', color='#FF1493')
plt.plot(df.loc[x,['sma20']], label='SMA20', color='#7FFF00')
#plt.plot(df.loc[x,['sma(20)']])




plt.legend()

plt.show()







"""
y1 = df.iloc[:,0]
y2 = df.iloc[:,1]
y3 = df.iloc[:,2]
#x = df.iloc[:,3]

plt.plot(x, y1, label='close price')
plt.plot(x, y2, label='SMA(50)')
plt.plot(x, y3, label='SMA(20)')

#plt.xlabel(x)
plt.ylabel('price')
plt.legend()


plt.show()
"""