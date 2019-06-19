str = "The greatest victory is that which requires no battle"

def reverse(string):
  strIntoList = string.split()
  revList = list(reversed(strIntoList))
  return " ".join(revList)

def reverseAlternative(string):
    return " ".join(string.split()[::-1])

print(reverse(str))
print(reverseAlternative(str))

## CHECKED