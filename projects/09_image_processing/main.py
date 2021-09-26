# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:12:10 2021

@author: Saeed
"""
from PIL import Image
from visualization import show_image_pair, show_four_images
from image_utils import enhance_image
import os


''' Read Image '''
image_path = 'images_input/(1).png'

try:
    img = Image.open(image_path)
except:
    print('Could not load file')

''' Rotate Image'''
# img_rotated = img.rotate(90)

''' Reduce Size '''
# Method 1
# img_resized = img.resize([img.width//2, img.height//2])
# Method 2
img_resized = img.reduce(2)

''' Enhance Image '''
# Brightness
img_brightened = enhance_image(img_resized, 'bri', 2)

# Contrast
img_contrasted = enhance_image(img_brightened, 'con', 1.5)

# Color
img_saturated = enhance_image(img_contrasted, 'col', 1.5)

''' Show Image '''
show_four_images(img_resized, img_brightened, img_contrasted, img_saturated)
show_image_pair(img_resized, img_saturated)


''' Save Image '''
try:
    out_dir = 'enhanced_images'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    
    input_filename = image_path.split('/')[-1]
    out_file = input_filename.split('.')[0] + '_enhanced.' + input_filename.split('.')[-1]
    new_file = os.path.join(out_dir, out_file)
    img_saturated.save(new_file, img.format)
except:
    print('Could not save file')
