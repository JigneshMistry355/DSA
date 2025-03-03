class ReverseArray:

    def naiveApproach(self, arr):
        temp_list = []
        
        for i in range(len(arr), 0, -1):
            temp_list.append(i)

        # alternative approach to copy array in reverse order
        # for i in range(len(arr)):
        #     temp_list[i] = arr[len(arr)-i - 1]
        
        for i in range(len(arr)):
            arr[i] = temp_list[i]

        return arr
    
    def twoPointerApproach(self, arr):
        n = len(arr)
        left = 0
        right = n-1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr

obj = ReverseArray()
result = obj.twoPointerApproach([1,2,3,4])
print(result)
