# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:47:52 2019

@author: saeed
"""
from time import time
from functools import reduce

start = time()
a = str(2**1000)

#a_i = map((lambda x: int(x)), a)
#s = reduce((lambda x, y: x+y), a_i)

a_i = [int(i) for i in a]
s = 0
for i in a_i:
    s += i

print(s)
print(time()-start)