# arr[i] > all elements to its right --> leader

def leaders(arr): 
    maxRight = arr[-1]
    result = []
    n = len(arr)
    for i in range(n-2, -1, -1): # start from n-2, till index 0 (reverse)
        if arr[i] > maxRight:
            maxRight = arr[i]
            result.append(maxRight)
    result.reverse()
    return result

arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))