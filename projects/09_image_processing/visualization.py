# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:13:06 2021

@author: Saeed
"""

import matplotlib.pyplot as plt


def show_image_pair(img1, img2, title1='Input Image', title2='Enhanced Image'):
    fig, ax = plt.subplots(1, 2)
    fig.suptitle('Image Enhancement with Pillow')

    ax[0].imshow(img1)
    ax[0].axis('off')
    ax[0].set(title = title1)

    ax[1].imshow(img2)
    ax[1].axis('off')
    ax[1].set(title = title2)

    plt.show()


def show_four_images(img1, img2, img3, img4):
    fig, ax = plt.subplots(2, 2)
    ax[0, 0].imshow(img1)
    ax[0, 0].axis('off')

    ax[0, 1].imshow(img2)
    ax[0, 1].axis('off')

    ax[1, 0].imshow(img3)
    ax[1, 0].axis('off')

    ax[1, 1].imshow(img4)
    ax[1, 1].axis('off')

    plt.show()
