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
    for k, v in cnt.items():
        if v >= 2:
            duplicates += 1
        
    return duplicates

print(countDuplicate(a))
print(countDuplicate(b))
print(countDuplicate(c))
print(countDuplicate(d))
print(countDuplicate(e))
print(countDuplicate(f))
print(countDuplicate(g))






