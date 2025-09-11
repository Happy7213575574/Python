import random as r
import time as t

numsPicked = []

while True:
  x = r.randint(1,90)
  #if x in numsPicked:
    #print('Redoing')
    #t.sleep(10)
  if len(numsPicked) >= 90:
    break
  else:
    print(x)
    numsPicked.append(x)
    print(len(numsPicked))#,'Thnis us bosfbhad')
    t.sleep(30)
#end while