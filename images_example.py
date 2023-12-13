# Images and Python
# Author: Pritika
# 13 December 2023

from PIL import Image

def pixel_to_string(pixel: tuple) -> str:
    """take a rgb 3 - tuple and "interpret it"
    as a colour and return that colour's name
    
    Params:
        pixel - 3-tuple of red (red,green,blue)
        
    return:
        string representing the colour.
        """

    r, g, b = pixel

    if g > 250 and r < 32 and b < 32:
        return"green"


# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # algorithm to visit every pixel in the kid-green image.

    # store the height and widhth of the image
    image_height = im.height
    image_width = im.width

    # top -> bottom
    for y in range(image_height):
        # left -> right 
        for x in range(image_width):
            # print out THIS PIXEL'S information
            pixel = im.getpixel((x,y))

            if pixel_to_string(pixel) == "green":
                print("GREENNN PIXELLLLLLLLLLLLLLLLLLL!!!!!!!!!!!!!")
            else:
                print("UNKNOWN PIXEL")


            print(pixel)




