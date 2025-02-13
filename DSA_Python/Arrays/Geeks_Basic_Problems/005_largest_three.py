def largestThree(arr):
    first = second = third = float('-inf')

    for i in range(len(arr)):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]

        elif arr[i] > third and arr[i] != second:
            third = arr[i]

    return [first, second, third]

arr =  [12, 35, 1, 10, 34, 1]


print(largestThree(arr))