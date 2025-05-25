#import modules
import turtle as tu
from turtle import Turtle as Tu

# Fullscreen the canvas
screen = tu.Screen()
screen.setup(1.0, 1.0)

#Make the person for turtle
person_shape = [
    (0, -20),    # bottom
    (0, 20),     # body up
    (-10, 40),   # left arm
    (0, 20),     # back to body
    (10, 40),    # right arm
    (0, 20),     # back to body
    (0, 60),     # neck
    (-10, 70),   # left side of head
    (-10, 80),   # top left
    (10, 80),    # top right
    (10, 70),    # right side
    (0, 60)      # close head
]

# Register and use the shape
tu.register_shape("stick_person", person_shape)

#make the turtle
t = Tu()
t.shape("stick_person")
tu.done()
t.speed(50) # set it's speed

t.setposition(0,0) #set the turtle

t.pensize(15) # make the pen thicker

#draw outline
radius = 200
t.color ('black')
t.circle(radius)

screen.mainloop() # make sure the screen does not turn off