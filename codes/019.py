# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 22:37:00 2019

@author: saeed
"""
from datetime import datetime

'''
for
>> datetime(y, m, 1).weekday()
Sunday is 6

for
>> datetime.isoweekday(datetime(y, m, 1))
Sunday is 7
'''

sundays = 0
for y in range(1901,2001):
    for m in range(1,13):
        w = datetime(y, m, 1).weekday()
        if w == 6:
            sundays += 1
            
print(sundays)