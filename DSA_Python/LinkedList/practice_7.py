class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def isEmpty(self):
        return self.head == None
    

    def getCount(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


    def insert_AtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    
    def insert_AtEnd(self, data):
        if self.isEmpty():
            self.insert_AtBeginning(data)
            return
        itr = self.head
        s = ''
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    def insert_At(self, index, data):
        if self.check_Index_Range(index):
            print("invalid Index in insert_At() function ")
        if index == 0 or self.isEmpty():
            self.insert_AtBeginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            itr = itr.next
            count += 1


    def check_Index_Range(self, index):
        return index < 0 or index >= self.getCount()


    # remove element from any index of the link list
    def remove_At(self, index):
        if (self.check_Index_Range(index)):
            print("Invalid index in remove_At()")
        if index == 0:
            itr = self.head
            itr.next
            self.head = itr.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1
        
            
    def displayList(self):
        itr = self.head
        s = ''
        while itr:
            s = s + str(itr.data) + '-->'
            itr = itr.next
        return s


if __name__ == '__main__':
    myList = LinkedList()
    myList.insert_AtBeginning(5)
    myList.insert_AtEnd(10)
    myList.insert_At(6,88)
    myList.insert_At(2,7)
    myList.remove_At(-2)
    print(myList.displayList())
    print(myList.getCount())
    # print(myList.check_Index_Range(-1))
