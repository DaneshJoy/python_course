'''
Using Pillow
'''
import matplotlib.pyplot as plt
from PIL import Image

# Read Image
file_path = 'baby.jpg'
im = Image.open(file_path)

# Visualization
im.show()

# Get image info
print(f'filename: {im.filename}')
print(f'format: {im.format}')
print(f'mode: {im.mode}')

# ~ Process
im = im.rotate(45)
im.show()

# Write Image
im.save('result_pil.png', format='PNG')

'''--------------------------------------'''
'''
Using Matplotlib
'''
# Read Image
file_path = 'old.jpg'
im2 = plt.imread(file_path)

# Visualization
plt.imshow(im2, cmap='gray')
plt.axis('off')
plt.show()

# Write Image
plt.savefig('result_plt.png', bbox_inches='tight')
