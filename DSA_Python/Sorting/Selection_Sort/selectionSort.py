def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        # hold minimum element index 
        min_idx = i
        # compare the remaining elements with new min_idx
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                # update the index of new samllest number 
                min_idx = j
        # swap element at the current index with the element at the newly found index  
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [4,6,3,1,2]
print("Unsorted :: ",arr)
print("Sorted :: ", selection_sort(arr))
print(arr)