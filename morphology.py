import numpy as np
from PIL import Image

def erode(img, kernel_size=3):
    image_array = np.array(img)
    height, width = image_array.shape

    radius = kernel_size // 2
    eroded_array = np.zeros_like(image_array, dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            y_min = max(y - radius, 0)
            y_max = min(y + radius + 1, height)
            x_min = max(x - radius, 0)
            x_max = min(x + radius + 1, width)

            roi = image_array[y_min:y_max, x_min:x_max]

            if np.sum(roi) == (kernel_size ** 2):
                eroded_array[y, x] = 1

    eroded_img = Image.fromarray(eroded_array * 255).convert('1')
    return eroded_img

def dilate(img, kernel_size=3):
    image_array = np.array(img)
    height, width = image_array.shape

    radius = kernel_size // 2
    dilate_array = np.zeros_like(image_array, dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            y_min = max(y - radius, 0)
            y_max = min(y + radius + 1, height)
            x_min = max(x - radius, 0)
            x_max = min(x + radius + 1, width)

            roi = image_array[y_min:y_max, x_min:x_max]

            if np.sum(roi) != 0:
                dilate_array[y, x] = 1

    dilate_img = Image.fromarray(dilate_array * 255).convert('1')
    return dilate_img

def opening(img, kernel_size=3):
    erode_img = erode(img, kernel_size)
    return dilate(erode_img, kernel_size)

def closing(img, kernel_size=3):
    dilate_img = dilate(img, kernel_size)
    return erode(dilate_img, kernel_size)