

import array as arr

class Sorting():

    def selectionSort(self, a):
        size = len(a)

        for i in range(0,size):
            min = i

            for j in range(i+1, size):
                if a[min] > a[j]:
                    min = j

            a[i], a[min] = a[min], a[i]

        return a
    
x = Sorting()
a = arr.array('i',[3,1,6,4,8])
print(a)
result = x.selectionSort(a)
print(result)