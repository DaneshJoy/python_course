# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 23:47:30 2019

@author: saeed
"""

f1 = 1
f2 = 2
sumAll = 2
while True:
    fn = f1 + f2
    if fn > 4000000:
        break
    if fn%2 == 0:
        sumAll = sumAll + fn
    f1 = f2
    f2 = fn

print('sum:', sumAll)
