# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:30:56 2019

@author: saeed
"""

import time
import numpy as np
start = time.time()

nums = [i for i in range(1,101)]
nums = np.array(nums, dtype='uint16')
sum_of_squares = np.sum(nums*nums)
square_of_sums = np.sum(nums)**2

print(int(square_of_sums - sum_of_squares))
print(time.time() - start)