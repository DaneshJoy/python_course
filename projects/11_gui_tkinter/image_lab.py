
import os
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance


class ImageLab:
    '''
    Image Processing Class

    Input: img_path
    '''

    def __init__(self, img_path):
        self.img_path = img_path
        self.filename = os.path.basename(self.img_path)
        self.filename.split('.')[-1]
        self.img = None
        self.result = None

    def load_image(self):
        try:
            self.img = Image.open(self.img_path)
        except Exception as e:
            print('Could not load file')
            print(e)

    def save_image(self, out_path):
        try:
            out_dir = out_path
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)

            out_file = self.filename.split('.')[0] + '_enhanced.' + self.format
            new_file = os.path.join(out_dir, out_file)
            self.result.save(new_file, self.format.upper())
        except Exception as e:
            print('Could not save file')
            print(e)

    def show_image(self, image):
        plt.imshow(image)
        plt.axis('off')
        plt.show()

    def show_result(self):
        self.show_image(self.result)

    def show_pair(self):
        fig, ax = plt.subplots(1, 2)
        fig.suptitle('Image Enhancement with Pillow')

        ax[0].imshow(self.img)
        ax[0].axis('off')
        ax[0].set(title='Input Image')

        ax[1].imshow(self.result)
        ax[1].axis('off')
        ax[1].set(title='Result')

        plt.show()

    def enhance_image(self, operation, factor):
        img_out = None

        if operation == 'bri':
            current_state = ImageEnhance.Brightness(self.img)
            img_out = current_state.enhance(factor)
        elif operation == 'col':
            current_state = ImageEnhance.Color(self.img)
            img_out = current_state.enhance(factor)
        elif operation == 'con':
            current_state = ImageEnhance.Contrast(self.img)
            img_out = current_state.enhance(factor)
        else:
            print('Invalid Operation')

        self.result = img_out
