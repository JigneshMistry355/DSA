class Queue:

    def __init__(self, size):
        self.size = size
        self.arr = []
        # self.front = self.arr[0]
        # self.rear = self.arr[len(self.arr)-1]

    
    def enqueue(self, data):
        if len(self.arr) >= self.size:
            print("Stack overflow")
            return 0
        self.arr[len(self.arr):] = [data]


    def dequeue(self):
        if len(self.arr) < 1:
            print("Stack underflow")
            return 0
        popped = self.arr[0]
        # rortate the array and delete the last element
        for i in range(1, len(self.arr)):
            self.arr[i-1] = self.arr[i]
        del self.arr[len(self.arr)-1]
        return popped
    

    def getFront(self):
        if len(self.arr) != 0:
            return self.arr[0]
        return -1
    
    def getRear(self):
        if len(self.arr) != 0:
            return self.arr[-1]
        return -1
    

        
q = Queue(5)
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q.arr)
q.dequeue()
print(q.arr)
print("Front : ", q.getFront())
print("Rear : ", q.getRear())




# different methods to append

# 1. concat 
# lst = []
# lst = lst + [1]
# print(lst) --> [1]

# 2. tuple unpacking
# lst = [] 
# lst = [*lst, 1, 2, 3]
# print(lst) # --> [1,2,3]