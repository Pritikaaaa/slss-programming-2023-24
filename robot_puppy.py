# Robot Puppy
# Author: Pritika Vats
# January 22, 2024

# Find the middle of the red ball
from PIL import Image
# Open up the image
ball_img = Image.open("./Images/red ball.jpeg")
red_pixels = []
# Visit every pixel finding the red ones
for y in range(ball_img.height):
    for x in range(ball_img.width):
        r, g, b = ball_img.getpixel((x, y))
        # Store the locations
        if r > 200 and g < 70 and b < 70:
            red_pixels.append((x, y))
# Isolate the xs
# Find the min and max x
# Same with ys
# Find the min and max y
min_x = min([x[0] for x in red_pixels])
max_x = max([x[0] for x in red_pixels])
min_y = min([x[1] for x in red_pixels])
max_y = max([x[1] for x in red_pixels])
# print(min_x, max_x)
# Do some math to find the midpoint of each
mid_x = min_x + (max_x - min_x) // 2
mid_y = min_y + (max_y - min_y) // 2
# Cross hair at result
ball_img.putpixel((mid_x, mid_y), (255, 255, 255))
ball_img.putpixel((mid_x + 1, mid_y), (255, 255, 255))
ball_img.putpixel((mid_x - 1, mid_y), (255, 255, 255))
ball_img.putpixel((mid_x, mid_y + 1), (255, 255, 255))
ball_img.putpixel((mid_x, mid_y - 1), (255, 255, 255))
ball_img.save("./Images/result_red_ball.jpeg")