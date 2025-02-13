def secondLargest(arr):
    mx = -1
    s_mx = -1
    for i in range(1, len(arr)):
        if arr[i] > mx:
            s_mx = mx
            mx = arr[i]

        elif arr[i] < mx and arr[i] > s_mx:
            s_mx = arr[i]
    return s_mx

arr =  [12, 35, 1, 10, 34, 1]


print(secondLargest(arr))