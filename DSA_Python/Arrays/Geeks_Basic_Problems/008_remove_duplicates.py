# using hash set
def removeDuplicate(arr: list[int]) -> int:
    seen = set()
    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx+=1

    return idx

# compare adjacent indices in sorted array
def removeDuplicates(arr: list[int]) -> int:
    idx = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[idx] = arr[i]
            idx+=1
    return idx




if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    result = removeDuplicates(arr)
    for i in range(result):
        print(arr[i], end=' ')
