# Make a rectangle with turtle

import turtle as tony

def rectangle(horizontal, vertical, color):
    tony.pendown() # put the pen down on the paper and start drawing

    # set some basics for our drawing - size color
    tony.pensize(1)
    tony.color(color)

    # actually begin
    tony.begin_fill()

    # the drawing of the famous rectangle
    for counter in range(1, 3)
        tony.forward(horizontal) # tony.forward(100) will make Tony the Turtle go 100 steps forward
        tony.right(90) # Tony turns 90 degrees to the right
        tony.forward(vertical)
        tony.right(90)

    # wind down, Tony!
    tony.end_fill()
    # stop drawing, you foolish turtle!
    tony.penup()