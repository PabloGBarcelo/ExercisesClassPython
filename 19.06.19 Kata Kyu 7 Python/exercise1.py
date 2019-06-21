def generateShape(number):
  for x in range(1,number+1):
    while x <= number:
      x+= 1
      print("x" * number)
      break
   
generateShape(5)