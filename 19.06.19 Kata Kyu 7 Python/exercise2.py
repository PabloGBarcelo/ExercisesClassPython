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