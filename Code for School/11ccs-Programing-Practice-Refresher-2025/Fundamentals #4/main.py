'''
using files to save data to and retrieve data from 

file operations are:- 
- open
- read
- write
- append
- close

syntax to open a file
https://www.w3schools.com/python/python_file_handling.asp

examples
*  students = open("students.txt","r")
*  scores = open("football_scores,"w+)
 
'''
scores = open("scores.txt","r") # file handle variable

eof = False			# set a boolean to track end of file

while not eof:

	scoreline = scores.readline()
	if scoreline == "": # end of file reached
		eof = True
	else:
		print(scoreline)
	#end if

#end while

scores.close() # close the file

	
	


