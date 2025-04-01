'''
# Sub Programs
Sub programs allow us to 'decompose' our programs into smaller pieces to make things easier to test and reuse
* procedures do not return data, functions do
* both procedures and functions can do one job W.O.R.M
* both procedures and functions take 'parameters' - data passed in
* we can call these procedures/functions as often as we like
## Example
On a calculator (embedded device), we can use function buttons to do calcualtions, eg. if we enter the number 2, then press the log(x) button, we get a result

covering the following Programming theory
* Arrays again
* Sub Programs
* Random Number Generation
* MOD and DIV again
'''

# arrays - there are 1D and 2D arrays and you can view these as grids with rows and columns for 2D

#declare variables
student_scores = [2,3,4,5,6,4,2,0,5,6]
student_scores[2] = "*"

#display list
print(student_scores)

#declare list
student_scores = [
	["Fred", 30],
	["Bob", 10],
	["Sarah", 20],
	["Tim", 12],
	["Drew", 2],
	["Zak",2]
]
#end list

#loop thorugh the list
for student in student_scores:
	print(student[1])
#end for

# a sub program is part of a program that we can reuse - often call a function - Python only has functions
# see notes file


#end def





# random number generation - allows us to get a random number in a range in case we wanted to use 'random-ness'

from random import randint as ri

