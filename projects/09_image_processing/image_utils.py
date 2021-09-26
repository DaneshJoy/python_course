# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:23:47 2021

@author: Saeed
"""

from PIL import ImageEnhance


def enhance_image(img, operation, factor):
    img_out = None

    if operation == 'bri':
        current_state = ImageEnhance.Brightness(img)
        img_out = current_state.enhance(factor)
    elif operation == 'col':
        current_state = ImageEnhance.Color(img)
        img_out = current_state.enhance(factor)
    elif operation == 'con':
        current_state = ImageEnhance.Contrast(img)
        img_out = current_state.enhance(factor)
    else:
        print('Invalid Operation')

    return img_out
        