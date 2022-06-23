

def hourglassSum(arr):
    # Write your code here
    newset = []
    for i in range(0,len(arr)-3):
        for j in range(0,len(arr)-2):
         value = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
         newset.append(value)
        max(newset)
    return max(newset)



array = [[-9, -9, -9,  1, 1, 1],
         [0, -9 , 0,  4, 3, 2],
         [-9, -9, -9,  1, 2, 3],
         [0,  0,  8 , 6, 6, 0],
         [0,  0 , 0 ,-2 ,0, 0],
         [0,  0 , 1 , 2, 4, 0]]

result = hourglassSum(array)