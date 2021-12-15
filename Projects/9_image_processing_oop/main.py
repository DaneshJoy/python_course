
import os
from image_enhancer import ImageEnhancer

images_dir = '../8_image_processing/images_input'
images_files = os.listdir(images_dir)

for f in images_files:
    # Create instance object from ImageEnhancer class
    my_image_enhancer = ImageEnhancer()
    
    # .. --> go back one directory
    my_image_enhancer.image_path = os.path.join(images_dir, f)
    my_image_enhancer.load_image()
    # my_image_enhancer.show_image()
    
    my_image_enhancer.enhance_image(2, 2, 2)
    my_image_enhancer.show_two_images()
    
    out_path = f.split('.')[0] + '_processed.png'
    my_image_enhancer.save_image(out_path)