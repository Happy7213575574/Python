def CollatzSequence():
  from GlobalFunctions import numberInput
  
  end = False
  
  print('This is a collatz sequence tester.')
  
  while end != True:
    print('Enter a zero to end the program')
    NumberInput = numberInput()
    Number = NumberInput

    # count the steps
    steps = 0
    print('bob')
    
    # do the squence
    for i in range(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
      if NumberInput == 0 or Number == 1:
        break
      elif  Number % 2 == 0:
        Number =  Number / 2
        steps = steps + 1
      elif Number % 2 != 0:
        Number = (3 * Number) + 1
        steps = steps + 1
      else:
        print('An error as occured')
      # end if
    #end for
              
    if  Number == 1:
        print("It took", steps, "steps")
    else:
        print("The  number didn't reach 1 yet")
    #end if
    return steps
#end def

CollatzSequence()
