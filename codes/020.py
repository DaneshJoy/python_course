# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:32:10 2019

@author: saeed
"""

def factorial(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

f = factorial(100)
s = str(f)
sumAll = 0
for i in range(len(s)):
    sumAll += int(s[i])
    
print(sumAll)