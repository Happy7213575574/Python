from tkinter import *
from tkinter import ttk
from tkinter import Tk

class tkinter:Tk(screenName='VcXsrv Server - Display Host', baseName=None, className='Tk', useTk=True, sync=False, use='1')

'''
import tkinter as tk

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
'''

''''
import os
import pymsgbox

pymsgbox.alert('Hi Afreeth ', 'Welcome')
if 'DISPLAY' not in os.environ: 
    pass
'''

'''
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :1.0')
    os.environ.__setitem__('DISPLAY', 'Display 1')
'''


import turtle as tu
from time import sleep as s

# Fullscreen the canvas
screen = tu.Screen()
screen.setup(1.0, 1.0)

#make the turtle
t = tu.Turtle()
t.shape('turtle') # set it's shape
t.speed(500 * 20 *40) # set it's speed

colours = ['alice blue', 'antique white', 'aquamarine', 'azure', 'beige', 'bisque', 'black','blanched almond', 'blue', 'blue violet', 'brown', 'burlywood', 'cadet blue','chartreuse', 'chocolate', 'coral', 'cornflower blue', 'cornsilk', 'crimson','cyan', 'dark blue', 'dark cyan', 'dark goldenrod', 'dark gray', 'dark green','dark khaki', 'dark magenta', 'dark olive green', 'dark orange', 'dark orchid','dark red', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray','dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dodger blue','firebrick', 'floral white', 'forest green', 'fuchsia', 'gainsboro', 'ghost white','gold', 'goldenrod', 'gray', 'green', 'green yellow', 'honeydew', 'hot pink','indian red', 'indigo', 'ivory', 'khaki', 'lavender', 'lavender blush', 'lawn green','lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod yellow','light green', 'light grey', 'light pink', 'light salmon', 'light sea green','light sky blue', 'light slate gray', 'light steel blue', 'light yellow', 'lime','lime green', 'linen', 'magenta', 'maroon', 'medium aquamarine', 'medium blue','medium orchid', 'medium purple', 'medium sea green', 'medium slate blue','medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue','mint cream', 'misty rose', 'moccasin', 'navajo white', 'navy', 'old lace','olive', 'olive drab', 'orange', 'orange red', 'orchid', 'pale goldenrod','pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff','peru', 'pink', 'plum', 'powder blue', 'purple', 'red', 'rosy brown', 'royal blue','saddle brown', 'salmon', 'sandy brown', 'sea green', 'seashell', 'sienna', 'silver','sky blue', 'slate blue', 'slate gray', 'snow', 'spring green', 'steel blue','tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white','white smoke', 'yellow', 'yellow green'] # list of colours to use

i = 0 # set the offest variable
left = 110 # set the angle varibles
right = 90
t.setposition(0,0)

for x in range(2): # make the loop to control
    for c in range(len(colours)):
        t.begin_fill() # start filling
        t.color(colours[c]) # set the colour
        t.left(left) # turn
        t.forward(200) # move forward
        t.left(right) # turn
        t.forward(200) # move forward

        print(colours[c])# show where it is in the list

        i += 1 # change the offset
        left -= i # apply the offset
        right -= i
        t.end_fill() # stop the fill for that colour
        
        if i < 5: # if offset greatetr than five reset the angles
            i = 1
            right = 110
            left = 90
#end for

t.speed(1) # change the speed
t.penup() # lift the pen up
t.setposition(-150, -15) # move the turtle
t.setheading(0) # set it's facing direction
t.pendown() # put the pen down

# make a circle
radius = 83 # set the radius
t.begin_fill() # start filling the circle
t.color('orange') # set the colour
t.circle(radius) # draw the cicrle
t.end_fill() # stop filling the circle

# make a out line
t.pensize(5) # make the pen thicker
t.color('black') # set the colour
t.circle(radius) # draw the circle

radius = -200
t.penup()
t.setposition(-163.29, 213.36)
t.setheading(20)
t.pendown()
t.begin_fill()
t.color ('cyan')
t.circle(radius)
t.end_fill()

radius = radius - 1
t.color ('black')
t.circle(radius)

t.hideturtle() # take the turtle off screen
s(30) #wait 30 seconds
screen.clear() # clear the screen

screen.mainloop() # make sure the screen does not turn off