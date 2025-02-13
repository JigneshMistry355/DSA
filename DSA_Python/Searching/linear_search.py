# mylist = [13, 9, 5, 4, 6, 2]
# find = 4
# for i in mylist:
#     if i == find:
#         print(f'found {find} at index {mylist.index(i)} \n')

# print(f'My list before: \n {mylist}')
# # sort method will change the existing list and doesn't return any value
# # mylist.sort(reverse = True)

# #sorted method doesn't change the existing list and returns a new sorted list
# print(f'My list after : \n {sorted(mylist, reverse = True)}')

#linear search loops approach
# def linearSearch(arr, length_of_list, query):

#     for i in range(0,length_of_list):
#         if arr[i] == query:
#             return i
#     return -1

# if __name__ == '__main__':

#     arr = [10, 5, 7, 6, 2]
#     query = 6
#     length_of_list = len(arr)

#     result = linearSearch(arr, length_of_list, query)
#     if result == -1:
#         print("Element not present in the list")
#     else:
#         print("Element present at index", result)
 

#linear search recursive approach

def linearSearchRecursive(arr, query, size):
    
    if size == 0:
        return -1
    elif arr[size - 1] == query:
        return size - 1
    else:
        return linearSearchRecursive(arr, query, size-1)


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    query = 4
    size = len(arr)

    result = linearSearchRecursive(arr, query, size)
    if result != -1:
        print(f'The element {query} is found at index {result}')
    else:
        print('Element not found !')