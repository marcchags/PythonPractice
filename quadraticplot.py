# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 09:58:40 2017

@author: marcc
"""

import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import seaborn as sns

print("please input a,b,c")
a = float(input())
b = float(input())
c = float(input())


def q(x):
	return((a*(x**2))+(b*x)+c)
	

print(q(-3))

xval = np.linspace(-10,10,100)
fig, ax = plt.subplots()
ax.plot(xval, q(xval))

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
