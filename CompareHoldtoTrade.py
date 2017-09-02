# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 10:45:18 2017

@author: marcc
"""

import pandas as pd
import numpy as np
import time
stime = time.time()

fname = input('Please enter csv filename: ')
   
df_orig = pd.read_csv(fname, header=0, parse_dates=True, index_col='Date')
df_orig = df_orig.drop(['High','Low', 'Volume'], axis='columns')
df_orig = df_orig.reindex(columns=['Open','Close'])


def setStats(df_orig, smadays, numsdbuy, numsdsell):
    """Calculates SMA, Bollinger bands (based on number of Std Devs 
    above/below SMA)"""
    df_stats = df_orig.copy()
    df_stats['sma'] = df_stats['Open'].rolling(window = smadays).mean()
    df_stats['smaplus'] = df_stats['sma'] + (numsdsell * (df_stats[
                'Open'].rolling(window=smadays).std()))
    df_stats['smaminus']= df_stats['sma'] - (numsdbuy * (df_stats[
                'Open'].rolling(window = smadays).std()))
    df_stats = df_stats[smadays:]
    return(df_stats)

def compareGains(df, perbuy, persell):
    """calculates trade amt based on rules already input in df. Columns
    must be in order: index is date, open, close,sma, sma+std, sma-std, 
    %amtbuy, %amtsell. Also, must only pass rows of df that HAVE SMA (ie must slice 
    dataframe before passing!)"""
    cash = 10000
    shares = 0
    buyholdcash = (int((cash/ df.iloc[1, 0])) * df.iloc[-1, 0])
   
    for a in range(1, len(df)):
        if df.iloc[a, 0] > df.iloc[a - 1,3]:
            #if open above sma+std, sell persell shares or as many as possible
            #at open price
            if shares > 1:
                quant = (int(shares * persell))
                if quant > shares or quant == 0:
                    quant = shares
                #print('sold ' + str(quant) + ' shares on '+ str(df.index[a].date()) + \
                 #     ' at ' + str(df.iloc[a, 0]))
                shares = shares - quant
                amt = quant * df.iloc[a, 0]
                cash = cash + amt
        elif df.iloc[a, 0] < df.iloc[(a - 1), 4]:
                #if open below sma-std, buy perbuy shares or as many 
                #as possible at open price
            if cash > df.iloc[a, 0]:
                
                if (perbuy * cash) > df.iloc[a,0]:
                   
                    #if perbuy*cash greater than stock price, follow rule
                    quant = int((perbuy * cash) / df.iloc[a, 0])
                    amt = quant * df.iloc[a, 0]
                    if amt > cash:
                        #if rounding causes amt to be greater than cash,
                        #reduce shares by 1
                        quant = quant - 1
                        amt = quant * df.iloc[a, 0]
                        shares = shares + quant
                        cash = cash - amt
                    else:
                        shares = shares + quant
                        cash = cash - amt
                    '''
                    print('bought ' + str(quant) + ' shares on ' + str(df.index[a].date()) + \
                          ' at ' + str(df.iloc[a,0]))
                    '''
				
                elif cash > df.iloc[a, 0]:
                    #if cash greater than 1 share but perbuy*cash less than
                    #open, purchase as many shares as possible
                    quant = int(cash / df.iloc[a, 0])
                    amt = quant * df.iloc[a, 0]
                    if cash - amt > 0:
                        cash = cash - amt
                        shares = shares + quant
                    else:
                        #if that causes a problem, buy 1 share
                        cash = cash - df.iloc[a, 0]
                        shares = shares + 1
                       
    amt = shares * df.iloc[-1, 0]
    cash = cash + amt
    return buyholdcash, cash

numsmadays_range = list(range(10, 51, 5))
numsdbuy_range = list(range(0, 5))
numsdsell_range = list(range(0, 5))

perbuy_range = list(np.arange(.1,.9, .1))
persell_range = list(np.arange(.1,.9,.1))

#df_results = pd.DataFrame(0,index = [0,1,2,3,4,5], columns=['a','b','c', \
#                    'd','e'])

list_data = [['buyhold','trade','sma','numsdbuy','numsdsell','perbuy','persell']]
for numdays in numsmadays_range:
    for numsdbuy in numsdbuy_range:
        for numsdsell in numsdsell_range:
            for perbuy in perbuy_range:
                for persell in persell_range:
                 
                    df = setStats(df_orig,numdays, numsdbuy, numsdsell)
                    df = df['2012':]
                    l1 = list(compareGains(df, perbuy, persell))
                    l1.append(numdays)
                    l1.append(numsdbuy)
                    l1.append(numsdsell)
                    l1.append(perbuy)
                    l1.append(persell)
                    list_data.append(l1)
            
    '''
    df = setStats(df_orig,numdays,stdbuynum, stdsellnum)
    df = df['2013':]
        
    l1 = list(compareGains(df, perbuy, persell))
    l1.append(numdays) #,stdsellnum,stdsellnum])
    l1.append(stdsellnum)
    l1.append(stdsellnum)
    list_data.append(l1)
    '''
    #df_results = df_results.append(pd.DataFrame(list_data, columns=['a','b','c', \
     #               'd','e']), ignore_index=True)

dfr = pd.DataFrame(list_data[1:], columns = list_data[0])

#print(dfr)
high = int(1)
z = 0
for a in range(0, len(dfr)):
    check = dfr.iloc[a, 1]
    if check > high:
        high = check
        z = a

print(dfr.iloc[[z]])
etime = time.time()

print(etime - stime)



