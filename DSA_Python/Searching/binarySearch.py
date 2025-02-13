def binarySearch(arr, query, low, high):

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == query:
            return mid

        elif arr[mid] < query:
            low = mid + 1

        else:
            high = mid - 1

    return -1
    

if __name__ == '__main__':
    arr = [10,20,30,40,50,60,70]
    query = 50
    low = 0
    high = len(arr)

    result = binarySearch(arr, query, low, high)

    if result != -1:
        print(f'Element {query} found at index {result}')
    else:
        print(f'Element {query} not found')

# bnary search recursive approach

def binarySearchRecursive(arr, query, low, high):
    if high >= low:
        mid = (low + high)//2

        if arr[mid] == query:
            return mid

        elif arr[mid] < query:
            return binarySearchRecursive(arr, query, mid+1, high)

        else:
            return binarySearchRecursive(arr, query, low, mid-1)

    else:
        return -1


if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60, 70]
    query = 3
    low = 0
    high = len(arr)

    result = binarySearchRecursive(arr, query, low, high)
    if result != -1:
        print(f'Element {query} found at index {result}')
    else:
        print(f'Element {query} not found !')