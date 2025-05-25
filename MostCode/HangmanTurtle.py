#import modules
import turtle as tu
from turtle import Turtle as Tu

# Fullscreen the canvas
screen = tu.Screen()
screen.setup(1.0, 1.0)

screen.addshape("person.gif")  # Add your image file here

#make the turtle
t = Tu()
t.shape("person.gif")  # Set the turtle to use the image
tu.done()
t.speed(50) # set it's speed
t.setposition(0,0) #set the turtle

t.pensize(15) # make the pen thicker

#draw outline
radius = 200
t.color ('black')
t.circle(radius)

screen.mainloop() # make sure the screen does not turn off