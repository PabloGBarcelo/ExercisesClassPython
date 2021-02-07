from functools import reduce 

ls = [0, 1, 3, 6, 10] 

#Array 20,20,19,16,10,0 

def parts_sums(array):
    inArray = []
    inArray.append(array[0])   
    output = []
    for i in range(len(array)): 
        product = reduce((lambda x, y: x + y), array)#usar esto para sumar un tuple or list
        output.append(product)#creamos una lista en la cual vamos metiendo la suma de cada vuelta
        del array[0]#En cada iteración quitamos el primer elemento

    output.insert(len(output),inArray[0])
    return output 

print(parts_sums(ls))

'''

    

     arr = []
    arr.append(arg)    
    result = []
    while(arr):
        sum( i for i in arr)        
        result.append(arr)
        del arr[0]
    return result

'''