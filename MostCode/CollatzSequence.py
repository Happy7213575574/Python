from GlobalFunctions import numberInput

def CollatzSequence():
  end = False
  
  while end != True:
    # run function  numberInput
    NumberInput = numberInput()

    # count the steps
    steps = 0

    # do the squence
    for i in range(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
      if  NumberInput == 1 or NumberInput == 0:
        break
      elif  NumberInput % 2 == 0:
          NumberInput =  NumberInput / 2
          steps = steps + 1
      else:
          NumberInput = (3 * NumberInput) + 1
          steps = steps + 1
      # end if
    #end for
              
    if  NumberInput == 1:
        print("It took", steps, "steps")
    else:
        print("The  number didn't reach 1 yet")
    #end if
    return steps
#end def

CollatzSequence()