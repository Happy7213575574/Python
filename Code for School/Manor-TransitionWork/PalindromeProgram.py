"""
Palindrome program. Create a program that: 
o The program asks for a word to be entered by the user  
o Tells the user how many characters are in the word  
o Displays the word in reverse  
o Tells the user whether the word is a palindrome or not (it can be spelled the same 
backwards and forward) 
"""

valid = False

while valid != True:
    word = input('Please enter a word: ').lower()
    if word != '':
        valid = True
    elif word == '':
        print('Please enter a word')
    else:
        print('A error has occured.')
    # end if
# end while

print(f"""There are {len(word)} characters in the word, {word.capitalize()}
The word in reverse is {word[::-1].capitalize()}
    """)

if word[::-1] == word:
    print(f"The word, {word.capitalize()}, is a palindrome.")
elif word[::-1] != word:
    print(f"The word, {word.capitalize()}, is not a palindrome.")