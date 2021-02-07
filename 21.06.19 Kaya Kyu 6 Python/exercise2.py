
'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

'''
import re
string = "The sunset sets at twelve o' clock."
## String to lowercase
## recorrerias cada uno
# convertirias al valor con algoritmo
# devuelves el array
# regex: [a-zA-Z]
## Result https://regex101.com/

def alphabetToNumber(string):
  lettersList = []

  for i in re.findall('[a-zA-Z]',string.lower()):
    lettersList.append(str(ord(i)-96))
  return " ".join(lettersList)

print(alphabetToNumber(string))