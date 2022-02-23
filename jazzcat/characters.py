from PIL import Image, ImageFont, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import os.path

def get_bitmap(text):
    path, _ = os.path.split(__file__)
    font = ImageFont.truetype(os.path.join(path, "VT323-Regular.ttf"), 11)

    s = font.getsize(text)

    # Draw font on simple image
    img = Image.new("1", s, (0,))
    d = ImageDraw.Draw(img)
    d.text((0, 0), text, (255,), font=font)

    img = np.array(img)
    if img.shape[1] > 51:
        raise Exception("String larger than one year!")

    return img[-7:, :]

def plt_bitmap(bmp):
    plt.matshow(bmp)
    plt.show()

if __name__ == '__main__':
    bmp = get_bitmap("ROY VORSTER")
    plt_bitmap(bmp)
