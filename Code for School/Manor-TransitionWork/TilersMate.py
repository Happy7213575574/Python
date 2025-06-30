"""
Create a program that:  
o Asks the user to enter the width and length of the floor to be tiled  
o Enter the cost per square metre of the tiles to be used  
o Calculate the cost of the tiles to be purchased  
o Calculate the length of time it would take a tiler to complete the task (1 hour for 
every 2 metres squared of tiling)  
o Calculate the cost of the entire job (tiles + labour) and display this without VAT 
and with VAT (an additional 20%) 
"""
#decalare variables
VAT = 1.20 # set VAT rate
valid = False # to control "while" loops

# create a while loop to get the length
while valid != True: # use a loop to validate user input
    try: # check that the input is a number
        length = int(input("What is the length of the floor to be tiled?: ")) # get the length of the room
        if str(length) != "": # perform a presence check
            valid = True # end the loop
        elif str(length) == "": # perform a presence check
            print('You must enter a number') # tell the user that it can not be blank
        else: # last resort for errors
            print("An error has occured.") # tell the user something has gone wrong
    except ValueError: # check the input can be a number
        print("Please enter a number.") # tell the user that a number must be inputed
# end while loop

valid = False # reset variable

# create a while loop to get the width
while valid != True: # use a loop to validate user input
    try: # check that the input is a number
        width = int(input("What is the length of the floor to be tiled?: ")) # get the width of the room 
        if str(length) != "": # perform a presence check
            valid = True # end the loop
        elif str(length) == "": # perform a presence check
            print('You must enter a number') # tell the user that it can not be blank
        else: # last resort for errors
            print("An error has occured.") # tell the user something has gone wrong
    except ValueError: # check the input can be a number
        print("Please enter a number.") # tell the user that a number must be inputed
# end while loop

valid = False # reset variable

# create a while loop to get the price per sqaure meter of tile
while valid != True: # use a loop to validate user input
    try: # check that the input is a number
        price = int(input("What is the price per sqaure meter of tile?: ")) # get the price per sqaure meter of tile
        if str(length) != "": # perform a presence check
            valid = True # end the loop
        elif str(length) == "": # perform a presence check
            print('You must enter a number') # tell the user that it can not be blank
        else: # last resort for errors
            print("An error has occured.") # tell the user something has gone wrong
    except ValueError: # check the input can be a number
        print("Please enter a number.") # tell the user that a number must be inputed
# end while loop

# create a while loop to get the price of labour per hour
while valid != True: # use a loop to validate user input
    try: # check that the input is a number
        labourPrice = int(input("What is the price of labour per hour?: ")) # get the price of labour per hour
        if str(length) != "": # perform a presence check
            valid = True # end the loop
        elif str(length) == "": # perform a presence check
            print('You must enter a number.') # tell the user that it can not be blank
        else: # last resort for errors
            print("An error has occured.") # tell the user something has gone wrong
    except ValueError: # check the input can be a number
        print("Please enter a number.") # tell the user that a number must be inputed
# end while loop

area = length * width # caculate the area of the room
cost = area * price # caculate the price of the tiles