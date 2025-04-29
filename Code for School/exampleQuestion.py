def checkdiscount(price, code):
    newprice = price 
    size = len(discount)
    for x in range(0, size):
        if discount[x][0] == code:
            newprice = newprice -  discount[x,1]
        else:
            x += 1
        #endif
    return newprice
#endfunction


discount = ['PVFC7', 10], ['CPU5', 5], ['BGF2', 15]

total = 0
price = 1

while price != 0:
    price = int(input('What is your item price?: '))
    code = str(input('What is your discount code?: '))
    
    checkdiscount(price,code)