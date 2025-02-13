class Node:
    
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None


    def printList(self):
        if self.isEmpty():
            print("The list is empty")
        
        itr = self.head
        list_str = ''
        while itr:
            list_str = list_str + str(itr.data) + '-->'
            itr = itr.next
        print(list_str)
        

    def isEmpty(self):
        return self.head == None
    

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    

    def checkIndex(self, index):
        if index < 0 or index > self.getLength():
            print("invalid Index")


    def insert(self, data, index):
        self.checkIndex(index)
        if index == 0:
            self.insertAtBeginning(data)
        itr = self.head
        count = 0 
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            itr = itr.next
            count += 1


    def removeAt(self, index):

        self.checkIndex(index)

        if index == 0:
            itr = self.head
            itr.next
            self.head = itr.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1


    def appendNode(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


if __name__ == '__main__':

    myList = LinkedList()
    myList.insertAtBeginning(4)
    myList.insert(5,1)
    myList.insert(9,2)
    myList.removeAt(4)
    myList.appendNode(10)
    myList.printList()
    print(myList.getLength())