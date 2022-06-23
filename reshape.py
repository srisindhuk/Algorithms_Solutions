import numpy as np
def changeshape(arr):
    arr = np.array(arr,int)

    return np.reshape(arr,(3,3))


arr = input().strip().split('\n')
print(changeshape(arr))