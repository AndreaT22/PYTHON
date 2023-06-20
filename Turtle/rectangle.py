# Make a rectangle with turtle

import tkinter
import turtle as tony

def draw_the_rectangle(horizontal, vertical, color):
    
    # set some basics for our drawing - size color
    tony.pensize(1)
    tony.color(color)
    tony.speed('fast')
    tony.bgcolor('pink')

    # actually begin
    tony.pendown() # put the pen down on the paper and start drawing
    tony.begin_fill()

    # the drawing of the famous rectangle
    
    for counter in range(1, 3):
        tony.forward(horizontal) # tony.forward(100) will make Tony the Turtle go 100 steps forward
        tony.right(90) # Tony turns 90 degrees to the right
        tony.forward(vertical)
        tony.right(90)

    # wind down, Tony!
    tony.end_fill()
    # stop drawing, you foolish turtle!
    tony.penup()


# draw 2 boxes
tony.penup()
#tony.goto(-100, -150)
#draw_the_rectangle(50,20, 'blue')
#tony.goto(-30, -150)
#draw_the_rectangle(50,20, 'blue')

#tony.goto(0,0)
#draw_the_rectangle(10,10, 'red')
#tony.goto(10,10)
#draw_the_rectangle(10,10, 'red')

for counter in range (0, 100, 10):
    tony.goto(counter,counter)
    draw_the_rectangle(10,10, 'red')

for counter in range (0, -100, -10):
    tony.goto(counter,counter)
    draw_the_rectangle(10,10, 'forest green')



tkinter.mainloop()

