
from PIL import Image

''' Read Image '''

img_pil = Image.open('test.png')

''' Show Image '''
img_pil.show()


''' Process Image '''
img_pil_resized = img_pil.resize([450, 305])
img_pil_resized.show()


''' Save Image '''

img_pil_resized.save('test_pil.png', img_pil.format)
