class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def isEmpty(self):
        return self.head == None
            
    def printEmptyList(self):
        return 'The list is empty'
        
    def getCount(self):
        if self.isEmpty():
            return 0
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_at_end(self, data):
        if self.isEmpty():
            self.insert_at_beginning(data)
        itr = self.head 
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def checkIndex(self, index):
        if index < 0 or index > self.getCount():
            print("Index out of range")
            return

    def insert_at(self, index, data):
        self.checkIndex(index)
        if index == 0:
            self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            itr = itr.next
            count += 1

    def insert_from(self, index, mylist):
        if self.isEmpty():
            return self.printEmptyList()
        self.checkIndex(index)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                for data in mylist:
                    itr.next = Node(data, itr.next)
                    itr = itr.next
            itr = itr.next
            count += 1

    def insertList_at_end(self, mylist):
        if self.isEmpty():
            for data in mylist:
                self.insert_at_end(data)
        
        itr = self.head
        while itr.next:
            itr = itr.next
        for data in mylist:
            itr.next = Node(data, itr.next)
            itr = itr.next

    def remove_at(self, index):
        if self.isEmpty():
            return self.printEmptyList()
        self.checkIndex(index)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def dropList(self):
        self.head = None
        return

    def printList(self):
        if self.isEmpty():
            return self.printEmptyList()
        itr = self.head
        stringText = ''
        while itr:
            stringText = stringText + str(itr.data) + '-->'
            itr = itr.next
        return stringText


if __name__ == '__main__':
    l = LinkedList()
    l.insert_at_beginning(4)
    l.insert_at_end(10)
    l.insert_at_beginning(1)
    l.insert_at(1,2)
    l.insert_at(4,11)
    l.insert_at(0,"Begin")
    l.insert_at(6, [1,2,3])
    l.insert_from(1,['A','B','C'])
    l.insertList_at_end([12,13,14,15])
    l.remove_at(2)
    print(l.printList())
    print(f'Size of LinkedList is {l.getCount()} ...')
    l.dropList()
    print(l.printList())
    print(f'Size of LinkedList is {l.getCount()} ...')