import re
from collections import Counter

a = "abcde"
b = "aabbcde"
c = "aabBcde" 
d = "indivisibility"
e = "Indivisibilities" 
f = "aA11" 
g = "ABBA"

def countDuplicate(text):
    
    duplicates = 0
    cnt = Counter()
    for i in text.lower():
         cnt[i]+=1
         if cnt[i]>=2:
             duplicates+=1         
        
    return duplicates

print(countDuplicate(e))







