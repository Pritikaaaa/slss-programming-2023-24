# Turtle Example
# Author: Pritika Vats
# November 21, 2023

import turtle

# Create a turtle that can move around the screen

FORWARD_MAGNITUDE = 20

# Make a turtle
michaelangelo = turtle.Turtle()

# get some input from the user
print("""To give command, type:
F - to go forward
L - to turn left
R - to turn right.""")

# repeat the below forever, or until the 
done = False


while not done:
    command = input("Where should I go? ").strip(",.?! ").lower()

    # move the turtle around based on the input 
    # stop if the user say stop
    if command in ["f", "forward"]:
        michaelangelo.forward(FORWARD_MAGNITUDE)
    elif command in ["r", "right"]:
        michaelangelo.right(90)
    elif command in ["l", "left"]:
        michaelangelo.left(90)
    elif command == "stop":
        done = True

