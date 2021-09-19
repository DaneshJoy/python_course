# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:08:22 2021

@author: Saeed
"""

import numpy as np
import scipy.io as sio
from scipy import signal
import matplotlib.pyplot as plt

''' --->> Load Data <<--- '''
ecg_data = sio.loadmat('202m (9).mat')
ecg_data = ecg_data['val']
print(ecg_data.shape)

''' ---> Plot Data <<---'''
ecg_data = ecg_data.transpose()
# plt.plot(ecg_data)
# plt.show()


''' --->> Find R Peaks <<--- '''
ecg_data = np.squeeze(ecg_data)
peaks = signal.find_peaks(ecg_data, height=1300)[0]

''' --->> Show Peaks on signal <<---'''
plt.plot(ecg_data, label='ECG Signal')
plt.scatter(peaks, ecg_data[peaks], c='m', marker='v', s=90, label='R Peaks')
plt.legend(loc='upper left')

plt.show()






