# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:58:20 2021

@author: Saeed
"""

import pandas as pd


def calculate_bmi(w, h):
    h /= 100
    bmi = w / (h**2)
    return bmi


''' --->> Read data <<--- '''
data = pd.read_csv("hw_200.csv")
# get Heights and Weights in separate lists
heights_list = data.iloc[:, 1].to_list()
weight_list = data.iloc[:, 2].to_list()

''' --->> Convert to cm and <<---  '''
# Method 1
# inch * 2.54 = cm
# pound / 2.205 = kg
# heights_list_cm = []
# for h in heights_list:
#    heights_list_cm.append(h * 2.54)

# Method 2
heights_list_cm = [(h*2.54) for h in heights_list]
weight_list_kg = [(w/2.205) for w in weight_list]

''' --->> Calculate BMI <<--- '''
bmis = []

# Method 1
# for i in len(heights_list_cm):
#    bmis.append(calculate_bmi(weight_list_kg[i], heights_list_cm))

# Method 2
for w, h in zip(weight_list_kg, heights_list_cm):
    bmis.append(calculate_bmi(w, h))
