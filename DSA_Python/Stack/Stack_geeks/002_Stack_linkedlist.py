class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, size):
        self.head = None
        self.size = size
        self.top = 0


    # Since it is a stack, we will insert and delete from head
    # The head will be top
    def push(self, data):
        if self.top >= self.size:
            print(f"Stack overflow \nCannot add more than {self.size} elements to the stack ")
            return
        self.head = Node(data, self.head)
        self.top += 1


    def pop(self):
        if self.isEmpty():
            return 
        itr = self.head
        itr = itr.next
        self.head = itr
        self.top -= 1

    def peek(self):
        return self.head.data



    def isEmpty(self):
        if self.head == None:
            print("The list is empty")
            return True
        return False
    

    # cannot use append in stack
    def append_element(self, data):
        if self.isEmpty():
            return
        itr = self.head 
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    def display(self):
        if self.isEmpty():
            return
        itr = self.head
        list_str = ''
        while itr:
            list_str = list_str + str(itr.data) + "-->"
            itr = itr.next
        print(list_str)


l = LinkedList(5)
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
l.push(6)
# l.push(7)
# l.append_element(6)
# l.display()
# l.pop()
l.display()
print(f"Top of the stack is {l.peek()}")
