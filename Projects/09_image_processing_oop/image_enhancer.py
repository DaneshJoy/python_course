from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt 

class ImageEnhancer:

    def __init__(self, img_path):
        self.image_path = img_path
        self.img = None
        self.img_output = None
    
    def load_image(self):
        try:
            self.img = Image.open(self.image_path)
        except:
            print('Can not load image')
    
    def show_image(self):
        plt.imshow(self.img)
        
    def save_image(self, output_path):
        try:
            self.img_output.save(output_path)
        except:
            print('Can not save image')
        
    def enhance_image(self, f_brightness, f_contrast, f_color):
        en_brightness = ImageEnhance.Brightness(self.img)
        img_brightness = en_brightness.enhance(f_brightness)
        
        en_contrast = ImageEnhance.Contrast(img_brightness)
        img_contrast = en_contrast.enhance(f_contrast)
        
        en_color = ImageEnhance.Color(img_contrast)
        self.img_output = en_color.enhance(f_color)
    
    def show_two_images(self):
        # Show multiple subplots
        fig, axs = plt.subplots(1,2)
        axs[0].imshow(self.img)
        axs[0].set_title('Input Image (Before)')
        axs[0].set_axis_off()
        axs[1].imshow(self.img_output)
        axs[1].set_title('Output Image (After)')
        axs[1].set_axis_off()
        
        