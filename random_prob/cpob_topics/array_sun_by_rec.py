def findSum(arr, N):
    if len(arr)== 1:
        return arr[0] 
    else:
        return arr[0]+findSum(arr[1:], N)

print(findSum([],0))