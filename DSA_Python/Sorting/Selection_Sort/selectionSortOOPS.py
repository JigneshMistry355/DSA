import array as arr
class Sorting():
    def __init__(self, ar):
        self.ar = ar
       
        

    def selectionSort(self):

        size = len(self.ar)

        for i in range(0, size):
            min = i

            for j in range(i+1, size):
                if min > self.ar[j]:
                    min = j

            self.ar[i], self.ar[min] = self.ar[min], self.ar[i]
        return self.ar
       
a = arr.array('i',[23,12,45,25,11,2])
s = Sorting(a)
x = s.selectionSort()
print(x)
      








