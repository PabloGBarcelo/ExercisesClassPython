nums = [1,'a','2',3,3,4,5,'b']
def findSecondLargest(aList):
  removeStr = [x for x in aList if not isinstance(x, str)]
  removeStr.sort()
  check = removeStr[-2]
  removeStr.remove(check)
  for i in removeStr:
    if removeStr == i:
      return "null"
    else:
      return check 

print(findSecondLargest(nums))

'''
nums = [1,'a','2',4,3,3,5,'b']

def findSecondLargest(aList):
  # Sort order
  removedStr = [x for x in aList if not isinstance(x, str)]
  removedStr.sort(reverse=1)
  ###### OK
  for x in range(len(removedStr)):
    if removedStr[0] > removedStr[x]:
      return None if removedStr[x] in removedStr[x+1:] \
                  else removedStr[x]
      #valor_si if condicion else valor_no

print(findSecondLargest(nums))
'''

