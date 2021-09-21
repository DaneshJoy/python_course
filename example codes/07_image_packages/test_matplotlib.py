# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:20:23 2021

@author: Saeed
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

''' Read Image '''

img_mpl = mpimg.imread('test.png')

''' Show Image '''
plt.imshow(img_mpl)
plt.show()


''' Process Image '''
# Matplotlib is not used for image processing


''' Save Image '''
plt.imsave('test_mpl.png', img_mpl)