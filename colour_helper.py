# Colour Helper
# Author: Pritika 
# December 12, 2023

# DO YOU NEED HELPPPP with colours?
# THIS is for you!!!!!!

def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name

    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if g > 250 and r < 32 and b < 32:
        return "green"
    
def is_light(pixel: tuple) -> bool:
    """returns  true if given picture is "light"
    
    Params:
        pixel - 3-tuple of values red, green, blue
        
    returns:
        True if pixel is light false if not
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
        return False



black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128, 128, 128)
red_pixel = (255, 90, 0)
white_pixel = (255, 255, 255)

# print(is_light(black_pixel))  # False
# print(is_light(dark_gray_pixel))  # False
# print(is_light(red_pixel)) # False
# print(is_light(light_gray_pixel))  # True
# print(is_light(white_pixel))  # True