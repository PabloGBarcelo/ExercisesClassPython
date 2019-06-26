array = [5,3,2,8,1,4,11]

def sort_array(a):
    newOddArr = []
    newEvenArr = []
    newSortedArr =[]
    for i in a:
        if i % 2 == 0:
            newEvenArr.append(i)
            
        else:
            newOddArr.append(i)
    newSortedArr.extend (sorted(newOddArr) + sorted(newEvenArr, reverse=True))
    return newSortedArr

print(sort_array(array))


