from PIL import ImageEnhance


def enhance_image(img, f_brightness, f_contrast, f_color):
    en_brightness = ImageEnhance.Brightness(img)
    img_brightness = en_brightness.enhance(f_brightness)
    
    en_contrast = ImageEnhance.Contrast(img_brightness)
    img_contrast = en_contrast.enhance(f_contrast)
    
    en_color = ImageEnhance.Color(img_contrast)
    img_output = en_color.enhance(f_color)
    
    return img_output