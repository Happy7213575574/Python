#declare variables
Coins =[['1p', 0.01], ['2p', 0.02], ['5p', 0.05], ['10p', 0.10], ['20p', 0.20], ['50p', 0.50], ['£1', 1.00], ['£2', 2.00]]
total = 0
valid = False

#open file to be written to
file = open("Digital Piggy Bank.txt", "w")

#run while loop until user enters X
while valid == False:
    coinInput = input("Enter a coin: ")
    
    #check input
    if coinInput == "X":
        print(f"You have £{total}.")
        file.write(str(total))
        file.close()
        valid = True
    
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
#end while
#end program
        