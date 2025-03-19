Coins =[['1p', 0.01], ['2p', 0.02], ['5p', 0.05], ['10p', 0.10], ['20p', 0.20], ['50p', 0.50], ['£1', 1.00], ['£2', 2.00]]
total = 0

valid = False

while valid == False:
    coinInput = input("Enter a coin: ")
    
    if coinInput == "exit":
        print(f"You have £{total}.")
        valid = True
    
    for i in range(len(Coins)):
        if coinInput == Coins[i][0]:
            total += Coins[i][1]
    
    print(f"You have £{total}.")
        