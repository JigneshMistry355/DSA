def checkIfSorted__ASC(arr):
    n = len(arr)

    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            return False
        
    return True

arr = [20, 20, 78, 98, 99, 97]
print(checkIfSorted__ASC(arr))