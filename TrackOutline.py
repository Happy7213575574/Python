"""
This code will do build a track map for Silverstone
"""
import turtle as tu

# Fullscreen the canvas
screen = tu.Screen()
screen.setup(100.0, 100.0)
screen.screensize(20000, 20000)

#Declare functions
def Circle(raduis, extent):
    r = raduis
    e = extent
    t.begin_fill
    t.circle(r, e)
#end def

def Silverstone():
    t.pensize(5)
    t.speed(0)
    #screen.delay(500)
    
    #Sector 1
    t.color("Red")
    
    #Start/Finish straight
    t.forward(400)
    print("Pit")
    t.write("Start")

    #T1
    Circle(-60, 45)
    print("T1")
    t.write("T1")
    
    #Straight
    t.forward(100)
    print("STRA")
    t.write("STRA")

    #T2
    Circle(80, 35)
    print("T2")
    t.write("T2")
    
    #Straight
    t.forward(100)
    print("STRAI")
    t.write("STRAI")

    #T3 
    Circle(-1, 90)
    print("T3")
    t.write("T3")
    
    #Straight
    t.forward(60)
    print("GAP1")
    t.write("GAP1")

    #T4
    Circle(10, 110)
    print("T4")
    t.write("T4")
    
    #T5
    Circle(40, 50)
    print("T5")
    t.write("T5")
    
    #Straight A
    t.forward(355)
    print("Well")
    
    #Sector 2
    t.color("Blue")
    
    #Straight B
    t.forward(50)
    print("ington")
    t.write("Wellington")
    
    #T6
    Circle(70, 70)
    t.write("T6")
    print("T6")

    #Straight
    t.forward(18)
    t.write("STRAI")
    print("STRAI")

    #T7
    Circle(-70, 170)
    t.write("T7")
    print("T7")

    # Hangar Straight
    t.forward(50)
    t.write("Hanger")
    print("Hang")

    #T8
    Circle(-30, 30)
    t.write("T8")
    print("T8")
    
    #National Pits
    t.forward(450)
    print("Nat")
    t.write("National Pits")
    
    #screen.delay(500)
    
    #T9
    Circle(-150, 50)
    print("T9")
    t.write("T9")
    
    #S2
    t.forward(200)
    print("S2")
    t.write("S2")
    
    #T10
    Circle(-180, 60)
    print("T10")
    t.write("T10")
    
    #T11
    Circle(-50, 60)
    print("T11")
    t.write("T11")
    
    #Straight
    t.forward(50)
    print("ST")
    t.write("ST")
    
    #T12
    Circle(50, 60)
    print("T12")
    t.write("T12")
    
    #Straight
    t.forward(30)
    print("STRAIG")
    t.write("STRAIG")
    
    #T13
    Circle(-50, 60)
    print("T13")
    t.write("T13")
    
    #Straight
    t.forward(60)
    print("STRAIG2")
    t.write("STRAIG2")
    
    #T14
    Circle(50, 60)
    print("T14")
    t.write("T14")
    
    #Sector 3
    t.color("Yellow")
    
    #Straight
    t.forward(700)
    print("ST2")
    t.write("ST2")

    #T15
    Circle(-100, 70)
    print("T15")
    t.write("T15")
    
    #Straight
    t.forward(50)
    print("STRAGIH")
    t.write("STRAGIH")
    
    #T16
    Circle(-130, 60)
    print("T16")
    t.write("T16")
    
    #T17
    Circle(-163, 50)
    print("T17")
    t.write("T17")
    
    """"
    #T18
    Circle(-180, 35)
    print("T18")
    t.write("T18")
    """
    
    #Straight
    t.forward(40)
    print("End")
    t.write("End")
    
    t.penup()
    t.right(90)
    t.forward(1000)
#end def  

#screen.addshape("F1Sprite1.gif")

#make the turtle
t = tu.Turtle()
t.shape('turtle') # set it's shape
t.speed(1) # set it's speed
scale = 0.5

t.penup()
t.setposition(0,0) #set the turtle

# setup
#tu.bgcolor("white")
t.pendown()
t.color("black")
t.pensize(10)

Silverstone()

screen.mainloop() #keep the screen on
