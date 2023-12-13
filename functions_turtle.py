# Functions and Turtles
# Author: Pritika
# November 28, 2023

import turtle

burt = turtle.Turtle()
burt.color("lightblue")

def squared(num: float) -> float:
    """takes a number and squares it."""

    return num ** 2
def draw_square(side_length: int) -> None:
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)


def draw_fancy_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height in pixels

    Params:

    level - number representing the level of branches
    height  - height of the main trunk in pixels.
    """

    if level > 0:
        #1. move turtle forward height pixels
        burt.forward(height)

        #a.  draw a smaller tree
        draw_fancy_tree(level -1, height * 0.75)

        #2. turn turtle left
        burt.left(36)

        #a. draw a smaller tree (current level -1)
        draw_fancy_tree(level -1, height * 0.75)

        #3. turn turtle right
        burt.right(36*2)
        draw_fancy_tree(level - 1, height * 0.75)

        #4. return to beginning
        burt.left(36)
        burt.back(height)
    else:
        original_color = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_color[0])

# Set-up Burt to draw trees
burt.color("brown")
burt.setheading(90)  # points burt north
burt.width(4)  # trunk and branches thicker
burt.speed(5)


draw_fancy_tree(4, 175)


turtle.done()