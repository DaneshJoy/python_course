# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:12:10 2021

@author: Saeed
"""
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt


''' Read Image '''
image_path = 'images_input/(1).png'
img = Image.open(image_path)

''' Show Image '''
plt.imshow(img)
plt.show()

''' Rotate Image'''
# img_rotated = img.rotate(90)

''' Reduce Size '''
# Method 1
# img_resized = img.resize([img.width//2, img.height//2])
# Method 2
img_resized = img.reduce(2)

''' Enhance Image '''
# Brightness
current_brightness = ImageEnhance.Brightness(img_resized)
img_brightened = current_brightness.enhance(2)

# Contrast
# TODO: Increase contrast

# Color
# TODO: Increase color

plt.figure()
plt.imshow(img_brightened)
plt.show()
