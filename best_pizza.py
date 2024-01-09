# Best Pizza
# Author: Pritika Vats
# December 19, 2023

import colour_helper

from PIL import Image

with Image.open("./Images/best_pizza.jpg") as im:
    image_height = im.height
    image_width = im.width

    for y in range(image_height):
        for x in range(image_width):
            # get the current pixel's information
            pixel = im.getpixel((x, y)) # tuple (r, g, b)

            # if the current pixel is light
            if colour_helper.is_light(pixel):
                # put a white pixel in its spot
                im.putpixel((x, y), colour_helper.white_pixel)
            else:  # if it's not
                # put a black pixel in its spot
                im.putpixel((x, y), colour_helper.black_pixel)

    im.save("./Images/binarized.jpg")
                
