import numpy as np
from PIL import Image
from morphology import erode, dilate, opening, closing

def debug_img():
    arr = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0],
        [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0],
        [0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
        [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ], dtype=np.uint8)
    return Image.fromarray(arr * 255).convert('1')

if __name__ == '__main__':
    # bin_img = debug_img()

    g_img = Image.open('images/symbol.png').convert('L')
    
    threshold = 128
    bin_img = g_img.point(lambda p: 255 if p > threshold else 0, mode='1')

    eroded = erode(bin_img, 3)
    eroded.show()

    dilated = dilate(bin_img, 3)
    dilated.show()

    opened = opening(bin_img, 3)
    opened.show()

    closed = closing(bin_img, 3)
    closed.show()