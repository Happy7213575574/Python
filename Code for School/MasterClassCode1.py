from random import randint as ri

def moveCharacter(direction,postion):
    if direction == 'left':
        postion -= 5
    if direction == 'right':
        postion += 5
        
    if postion >1:
        postion = 1
        return postion
    elif postion < 512:
        postion = 512
        return postion
#end def


p = ri(1, 512)
print("The position is ", p)
a = ""
while a != "left" and a != "right":
    a = input("Enter direction, left or right: ").lower()
#endwhile

moveCharacter(a,p)

print(f"""
      
New postion is {p}
      """)