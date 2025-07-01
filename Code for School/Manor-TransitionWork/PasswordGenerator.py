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
from random import randint as r

valid = False

letters = [
["q","w","e","r","t",'y','u','i','o','p','a','s','d','f','g','h','j','k','l','z''x','c','v','b','n','m'],
['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
]

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

while valid != False:
    strength = input("How strong would you like the password (weak, medium or strong)?:").lower()
    if strength == "weak" or strength == "medium" or strength == "strong":
        valid = False
    elif strength != "weak" or strength != "medium" or strength != "strong":
        print("Please pick how strong you would like the password, weak, medium or strong.")
    # end if
# end while

if strength == "weak":
    
elif strength == "medium":
    
elif strength == "strong":
    
else:
    print("You did not pick one of the options or an error has occured")