
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

''' Read Image '''

img_mpl = mpimg.imread('test.png')

''' Show Image '''
plt.imshow(img_mpl)
plt.show()


''' Process Image '''
# !!! We can't use matplotlib for image processing


''' Save Image '''
plt.imsave('test_mpl.png', img_mpl)
