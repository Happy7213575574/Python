#main code for digital piggy bank

#get previous ammount from file
#open file
#file = open("Coins.txt", "r")
file = open("Code for School/Coins.txt", "r")

#read file
data = file.read()
#end for

#close file
file.close()

#declare total
total = float(data)

#dispaly previous total
print(f"Your previous total was £{total}.")

#declare variables
Coins =[['1p', 0.01], ['2p', 0.02], ['5p', 0.05], ['10p', 0.10], ['20p', 0.20], ['50p', 0.50], ['£1', 1.00], ['£2', 2.00]]
valid = False

#run while loop until user enters X
while valid == False:
    coinInput = input("Enter a coin to add (enter X to end program): ").lower()
    
    #check input
    if coinInput == "x":
        print(f"You have £{total}.")
        valid = True
        #end while
    
    else:
        #caculate coin value
        for i in range(len(Coins)):
            if coinInput == Coins[i][0]:
                total += Coins[i][1]
                total = round(total, 2)
            #end if
        #end for
    #end if
    
    #print total
    print(f"You have £{total}.")
#open file to be written to and close file
file = open("Code for School/Coins.txt", "w")
file.write(str(total))
file.close()
#end program
