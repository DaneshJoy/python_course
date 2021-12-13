import matplotlib.pyplot as plt


def show_two_images(img, img_output):
    # Show multiple subplots
    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[0].set_title('Input Image (Before)')
    axs[0].set_axis_off()
    axs[1].imshow(img_output)
    axs[1].set_title('Output Image (After)')
    axs[1].set_axis_off()
