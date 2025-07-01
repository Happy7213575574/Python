"""
Random password generator. Create a program that:  
o Asks the user how many characters should be in the password  
o Asks the user how complex the password should be; weak, medium or strong  
o Creates a random password of the appropriate length to be the correct password 
strength 
▪ Weak passwords should be all letters  
▪ Medium passwords should include at least one number  
▪ Strong passwords should include at least one number and one special 
character ( + - / & ! ) 
o Display the suggested password 
"""

valid = False

while valid != True:
    try:
        length = int(input("How long should the password be?: "))
        if length == "":
            print("Please enter a number")
        elif length != "":
            valid = True
        # end if
    except ValueError:
        print("Please enter a number")
    # end try
# end while