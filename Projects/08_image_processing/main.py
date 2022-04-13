
from PIL import Image
from visualization import show_two_images
from image_utils import enhance_image


# Load Image
filepath = 'images_input/(4).png'
img = Image.open(filepath)

# Show image with Pillow
# img.show()

# Image Properties
print(f'Format: {img.format}')
print(f'Mode: {img.mode}')
print(f'Size: {img.size}')

# %% Image Enhancement
f_brightness = 2
f_contrast = 2
f_color = 2
img_output = enhance_image(img, f_brightness, f_contrast, f_color)

# %% Image Visualization
show_two_images(img, img_output)

# %% Save result
img_output.save("result2.png")


