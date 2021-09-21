# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:18:28 2021

@author: Saeed
"""
import cv2

''' Read Image '''

img_cv = cv2.imread('test.png')


''' Show Image '''
cv2.imshow('image', img_cv)
cv2.waitKey()
cv2.destroyAllWindows()


''' Process Image '''
img_cv_resized = cv2.resize(img_cv, (450, 305))

cv2.imshow('image', img_cv_resized)
cv2.waitKey()
cv2.destroyAllWindows()


''' Save Image '''

cv2.imwrite('test_cv.png', img_cv_resized)





