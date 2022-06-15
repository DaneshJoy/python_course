
from PIL import Image
from glob import glob
from visualization import show_two_images
from image_utils import enhance_image


# Load Image
filenames = glob('images_input/*.png')
for f in filenames:
    '''
    Read Image
    '''
    # TODO: Error handling (Use try/except)
    img = Image.open(f)

    # Show image with Pillow
    # img.show()

    # Image Properties
    print(f'Format: {img.format}')
    print(f'Mode: {img.mode}')
    print(f'Size: {img.size}')

    '''
    Enhance Image
    '''
    f_brightness = 2
    f_contrast = 2
    f_color = 2
    img_output = enhance_image(img, f_brightness, f_contrast, f_color)

    '''
    Visualization
    '''
    show_two_images(img, img_output)

    '''
    Save Results
    '''
    # TODO: Error handling (Use try/except)
    # TODO: Create a function for saving
    file_name = f.split('\\')[-1].split('.')[0]
    file_ext = f.split('\\')[-1].split('.')[1]
    out_file = file_name + '_en.' + file_ext
    img_output.save(out_file)


