#get previous ammount from file
file = open("dpb.txt", "r")

for line in file:
    data = file.readline()
file.close()
total = float(data)
print(f"Your previous total was £{total}.")

#declare variables
Coins =[['1p', 0.01], ['2p', 0.02], ['5p', 0.05], ['10p', 0.10], ['20p', 0.20], ['50p', 0.50], ['£1', 1.00], ['£2', 2.00]]
valid = False

#run while loop until user enters X
while valid == False:
    coinInput = input("Enter a coin (enter X to end program): ").lower()
    
    #check input
    if coinInput == "x":
        print(f"You have £{total}.")
        #open file to be written to and close file
        file = open("Coins.txt", "w")
        file.write(str(total))
        file.close()
        valid = True
        #end while
    
    else:
        #caculate coin value
        for i in range(len(Coins)):
            if coinInput == Coins[i][0]:
                total += Coins[i][1]
            #end if
        #end for
    #end if
    
    #print total
    print(f"You have £{total}.")
#end program
        