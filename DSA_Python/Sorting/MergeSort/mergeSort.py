# merge two sorted arrays
def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i,j,k = 0,0,0
    arr3 = [None for i in range(m+n)]
    while i < m and j < n:
        print(i)
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1  
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1
    while i < m:
        arr3[k] = arr1[i]
        i += 1
        k += 1

    while j < n:
        arr3[k] = arr2[j]
        j += 1
        k += 1

    return arr3


def merge1(arr, left, mid, right):
    n1 = mid-left+1
    n2 = right - mid

    L = [0]*n1
    R = [0]*n2
 

    for i in range(n1):
        L[i] = arr[left+i]
    for j in range(n2):
        R[j] = arr[mid+1+j]

    print("Left arr : ", L)
    print("Right arr : ", R)

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge1(arr, left, mid, right)


def print_arr(arr):
    for i in arr:
        print(i, end=" ")
    print()

arr1 = [1,3,5,7,9,10,13,2,4,6,8,12,11]
# arr2 = [2,4,6,8,12,11]
# result = merge(arr1, arr2)
# print(len(arr1))
print_arr(arr1)
mergeSort(arr1, 0, len(arr1)-1)
print_arr(arr1)
