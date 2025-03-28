'''
Strings again

strings are like arrays

main syntax of commands here

https://www.w3schools.com/python/python_strings.asp
https://www.w3schools.com/python/python_strings_slicing.asp

'''

string = "abcdefghijklmnopqrstuvwxyz"

# write Python to extract and print the left 5 characters of the string above

print(string[0:5])

# do the same to get the middle 5 characters

print(string[10:15])

# now do the same to get the last 4 characters

print(string[-4:])

# what is the command to find the length of a string ?

length = len(string)
print(length)

# what is the command to reverse a string in Python ?

ReverseString = string[::-1]
print(ReverseString)

#end program