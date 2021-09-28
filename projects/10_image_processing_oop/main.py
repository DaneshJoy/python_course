# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:26:01 2021

@author: Saeed
"""

from image_lab import ImageLab


image_path = '../09_image_processing/images_input/(1).png'

img_lab1 = ImageLab(image_path)
img_lab1.load_image()
img_lab1.show_image(img_lab1.img)

img_lab1.enhance_image('bri', 2.0)
img_lab1.show_pair()

img_lab1.img = img_lab1.result
img_lab1.enhance_image('con', 1.5)
img_lab1.show_pair()
