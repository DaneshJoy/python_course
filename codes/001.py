# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 23:43:00 2019

@author: saeed
"""

n = 1000
sumAll = 0
for i in range(3,n):
    if i%3 == 0 or i%5 ==0:
        sumAll += i
        
print(sumAll)