def generateShape(number):
  for x in range(1,number+1):
    while x <= number:
      x+= 1
      print("x" * number)
      break
   
generateShape(5)
'''
def generateShape(number):
  for x in range(1,number+1):
    while x <= number:
      x+= 1
      print("x" * number)

def printNumberOfTimes(number):
  string = "x"
  toReturn = ""
  for x in range(number):
    toReturn += string
  #print(toReturn)

  for x in range(number):
    print (toReturn)
  
  return

printNumberOfTimes(5)  
#generateShape(5)
'''