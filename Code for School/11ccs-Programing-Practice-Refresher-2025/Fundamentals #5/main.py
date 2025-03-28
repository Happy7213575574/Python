'''
covering the following Programming theory
* Arrays again
* Sub Programs
* Random Number Generation
* MOD and DIV again
'''

# arrays - there are 1D and 2D arrays and you can view these as grids with rows and columns for 2D

student_scores = [2,3,4,5,6,4,2,0,5,6]
student_scores[2] = "*"
print(student_scores)

student_scores = [
	["Fred", 30],
	["Bob", 10],
	["Sarah", 20],
	["Tim", 12],
	["Drew", 2],
	["Zak",2]
]

for student in student_scores:
	print(student[1])

# a sub program is part of a program that we can reuse - often call a function - Python only has functions
# see notes file


#end def





# random number generation - allows us to get a random number in a range in case we wanted to use 'random-ness'

from random import randint as ri




