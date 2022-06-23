import numpy

def arrays(arr):


    arr.reverse()
    return numpy.array(arr,float)

arr = input().strip().split(' ')
print(arr)
result = arrays(arr)
print(result)

