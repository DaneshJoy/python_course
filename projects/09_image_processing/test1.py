from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt

# # load input data
file_path = 'images_input/(4).png'
img = Image.open(file_path)

# method 1
img_resized = img.resize([img.width//2, img.height//2])
# method 2
img_resized = img.reduce(2)

# Enhance Brightness
curr_bri = ImageEnhance.Brightness(img_resized)
img_brightened = curr_bri.enhance(1.5)

# Enhance Contrast
curr_con = ImageEnhance.Contrast(img_brightened)
img_contrasted = curr_con.enhance(1.5)

# Enhance Color Level
curr_col = ImageEnhance.Color(img_contrasted)
img_colored = curr_col.enhance(2.0)


plt.suptitle('Image Enhancement')
plt.subplot(2,2,1)
plt.imshow(img_resized)
plt.axis('off')
plt.title('Input Image')

plt.subplot(2,2,2)
plt.imshow(img_brightened)
plt.axis('off')
plt.title('Brightness')

plt.subplot(2,2,3)
plt.imshow(img_contrasted)
plt.axis('off')
plt.title('Brightness + Contrast')

plt.subplot(2,2,4)
plt.imshow(img_colored)
plt.axis('off')
plt.title('Brightness + Contrast + Color')

plt.show()

plt.figure()
plt.suptitle('Image Enhancement')
plt.subplot(1,2,1)
plt.imshow(img_resized)
plt.axis('off')
plt.title('Input Image')

plt.subplot(1,2,2)
plt.imshow(img_colored)
plt.axis('off')
plt.title('Brightness + Contrast + Color')

# img_gray = img.convert('L')
# plt.figure()
# plt.imshow(img_enhanced, cmap='gray')
# plt.show()

