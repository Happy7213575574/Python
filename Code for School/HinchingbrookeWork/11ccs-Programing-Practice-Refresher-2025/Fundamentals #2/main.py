'''
short program to remind us of the following basics:-

* Operators - DIV and MOD
* 
* Functions
* Strings functions 
   - CONCATENATION - joining strings together using '+'
   - MID, LEFT and RIGHT
      -- access any part of a string - there is no provision in Python, 
      so we have to use string SPLICING methid using [x:y:z]
   - LEN() = get length of a string
   - UPPER() = convert a string to upper case
   - LOWER() = convert a string to lower case
   - Searching a String using iteration
'''

# lets look at mod and div and how they work
# both are mathematical operators - only on work on numbers, not strings

# MOD in Python is % symbol, A % B --> remainder

num = 11 % 2
print(num)

# DIV in Python is // symbol, A // B --> quotient

num = 11 // 2
print(num)

'''
string concatention using '+' operator
'''

SentenceA = "Hello"
SentenceB = "Person"

setenceC = SentenceA + " " + SentenceB

print(setenceC)

# lets conver the string above ot upper and lowe case

UperCase = setenceC.upper()
LowerCase = setenceC.lower()

print(UperCase)
print(LowerCase)

# calculate the length of string - integer

length = len(setenceC)
print(length)

'''
let's split a string
* LEFT(n)
* RIGHT(n)
* MID(start,stop)

these are not available in Python, we use [start:end]
'''

# calcualte how to extract just the surname!

# lets' dynamically get the surname from any full name
# ask for input of full name and use the .find() methid to search for a space then extract the name

name = input("Enter your full name: ")
space = name.find(" ")
surname = name[space+1:]
print(surname)

#end program